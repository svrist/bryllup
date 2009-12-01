from google.appengine.ext import db

class Gaest(db.Model):
  created = db.DateTimeProperty(auto_now_add=True)
  updated = db.DateTimeProperty(auto_now=True)
  navn = db.StringProperty(required=True)
  vaerelse = db.BooleanProperty(default=False)
  betalt = db.BooleanProperty(default=False)
  type = db.StringProperty(required=True, default="Sus",choices=['Sus','S&oslash;ren','Venner'])
