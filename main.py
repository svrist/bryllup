#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import wsgiref.handlers
import logging

from base_request_handler import BaseRequestHandler,main
from google.appengine.ext import webapp
from form import *

webapp.template.register_template_library('django_hack')


class MainHandler(BaseRequestHandler):
    def gencur(self,site):
        tt = "class=\"current\""
        if site == "brylluppet":
            return {"nav2": tt}
        elif site == "transport":
            return {"nav3": tt}
        elif site == "onsker":
            return {"nav4": tt}
        elif site == "overnatning":
            s = Seng.get()
            dobbelt = s.double
            enkelt = s.single
            return {"nav5": tt, "dobbelt":dobbelt,"enkelt":enkelt}
        elif site == "gaester" or site=="gaester2":
                       return ret
        else:
            return {"nav1" : tt}

    def get(self,site="index"):
        if site is "":
            site="index"
        self.generate("%s.html"%site,self.gencur(site))

class GaestHandler(BaseRequestHandler):
    def get(self):
        self.enforce_admin()
        vals = {}
        form = GaestForm()
        normal = True
        action = self.request.get('action')
        if self.request.get("id"):
            id = int(self.request.get("id"))
            g = Gaest.get(db.Key.from_path("Gaest",id))

        if action == "edit":
            form = GaestForm(instance=g)
            vals['id'] = id
            normal = False
        elif action == "del":
            g.delete()

        gaester = Gaest.all().order("type")
        vals['form'] = form
        vals['gaester'] = gaester
        vals['normal'] = normal
        self.generate("admin_gaest.html",vals)
    def post(self):
        form = GaestForm(data=self.request.POST)

        if self.request.get('_id'):
            id = int(self.request.get("_id"))
            g = Gaest.get(db.Key.from_path("Gaest",id))
            form = GaestForm(data=self.request.POST,instance=g)
        else:
            form = GaestForm(data=self.request.POST)

        if form.is_valid():
            form.save()
        self.redirect("/admin/gaest")

class GaestList(BaseRequestHandler):
    def get(self):
        ret = {}
        tt = "class=\"current\""
        ret["nav1"]= tt
        g = {}
        ret["gaester"] =  ["Susanne","S&oslash;ren","Venner"]
        ret["gaesterdict"] = {}
        for g in ret["gaester"]:
            ret["gaesterdict"][g] = Gaest.all().\
                    filter("type = ",g).\
                    filter("meldttilbage =", True).\
                    order("created").\
                    fetch(80)
            if len(ret["gaesterdict"][g]) %2 != 0:
                   ret["gaesterdict"][g].append("")
        self.generate("gaester.html",ret)

class GaestDescr(BaseRequestHandler):
    def get(self,id):
        id = int(id)
        g = Gaest.get(db.Key.from_path("Gaest",id))
        self.generate("gaestdescr.html",{'g':g})


class SengHandler(BaseRequestHandler):
  def get(self):
    f = SengForm(instance=Seng.get())
    self.generate("admin_seng.html",{'form':f})

  def post(self):
    f = SengForm(data=self.request.POST,instance=Seng.get())
    if f.is_valid():
      f.save()
    self.redirect("/admin/seng")

class WishList(BaseRequestHandler):
    def get(self):
        tt = "class=\"current\""
        l = {}
        l['nav4'] = tt
        l['wishs'] = Wish.all().fetch(1000)
        self.generate("onsker.html",l)

class WishListAdmin(BaseRequestHandler):
    def get(self,form=None):
        self.enforce_admin()
        vals = {}
        vals['wishs'] = Wish.all().order('position').fetch(1000)
        if form is None:
            if len(vals['wishs']) > 0:
                m = max([ w.position for w in vals['wishs'] ])+1
            else: 
                m = 1
            form = WishForm(initial={'position':m} )
        action = self.request.get('action')
        if self.request.get("id"):
            id = int(self.request.get("id"))
            g = Wish.get(db.Key.from_path("Wish",id))

        if action == "edit":
            form = WishForm(instance=g)
            vals['id'] = id
        elif action == "del":
            g.delete()

        vals['form'] = form
        self.generate("admin_onsk.html",vals)

    def post(self):
        if self.request.get('_id'):
            id = int(self.request.get("_id"))
            w = Wish.get(db.Key.from_path("Wish",id))
            form = WishForm(data=self.request.POST,instance=w)
        else:
            form = WishForm(data=self.request.POST)

        if form.is_valid():
            form.save()
            self.redirect("/admin/onsk")
        else:
            self.get(form)



class AdminHandler(BaseRequestHandler):
    def get(self):
        self.enforce_admin()
        self.redirect("/admin/gaest")

if __name__ == '__main__':
    application = webapp.WSGIApplication([
        ('/gaester',GaestList),
        ('/onsker',WishList),
        ('/gaest/(\d+)$',GaestDescr),
        ('/admin/gaest',GaestHandler),
        ('/admin/seng',SengHandler),
        ('/admin/onsk',WishListAdmin),
        ('/admin/?$',AdminHandler),
        ('/(.*)', MainHandler)], debug=True)
    main(application)
