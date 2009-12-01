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
            dobbelt = 11
            enkelt = 4
            return {"nav5": tt, "dobbelt":dobbelt,"enkelt":enkelt}
        elif site == "gaester" or site=="gaester2":
            ret = {}
            ret["nav1"]= tt
            g = {}
            sv = ["Mor og Far",
                  "Niels og Marie",
                 "Anne og Thomas",
                 "Eva",]
            ven = ["Maja og Anders","Pernille","Heidi", "Mette og Rasmus", "Simon og Marit"]
            sus = [ "Mor, Nicoline, Josephine",
                   "Malene og Michael",
                   "Doris og Frank",
                   "Thora og Mortensen, Pernille og Dorte",
                   "Charlotte og Claus",
                   "Ann-Mari og Mads",
                   "Lars og Mie",
                  ""]
            if len(sus) % 2 != 0:
                sus.append("")
            if len(sv) % 2 != 0:
                sv.append("")
            if len(ven) % 2 != 0:
                ven.append("")
            g["Susanne"]= sus
            g["S&oslash;ren"]= sv
            g["Venner"] = ven
            ret["gaesterdict"] =  g
            ret["gaester"] =  ["Susanne","S&oslash;ren","Venner"]
            return ret
        else:
            return {"nav1" : tt}

    def get(self,site="index"):
        if site is "":
            site="index"
        self.generate("%s.html"%site,self.gencur(site))

class GaestHandler(BaseRequestHandler):
  def get(self):
    form = GaestForm()
    gaester = Gaest.all()
    self.generate("admin_gaest.html",{'form':form, 'gaester':gaester})
  def post(self):
    form = GaestForm(data=self.request.POST)
    if form.is_valid():
      form.save()
      self.redirect("/admin/gaest")





if __name__ == '__main__':
    application = webapp.WSGIApplication([
      ('/admin/gaest',GaestHandler),
      ('/(.*)', MainHandler)], debug=True)
    main(application)
