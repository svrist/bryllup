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
            return {"nav5": tt}
        elif site == "gaester":
            ret = {}
            ret["nav1"]= tt
            g = {}
            sv = []
            ven = []
            sus = [ "Mor, Nicoline, Josephine",
                    "Doris og Frank",
                   "Thora og Mortensen",
                   "Karen og Jan",
                   "Helle og Kalle"]
            g["sus"]= sus
            g["sv"]= sv
            g["venner"] = ven
            ret["gaester"] =  g
            return ret
        else:
            return {"nav1" : tt}

    def get(self,site="index"):
        if site is "":
            site="index"
        self.generate("%s.html"%site,self.gencur(site))


if __name__ == '__main__':
    application = webapp.WSGIApplication([('/(.*)', MainHandler)],
                                         debug=True)
    main(application)
