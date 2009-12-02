from google.appengine.ext import db

class Gaest(db.Model):
  created = db.DateTimeProperty(auto_now_add=True)
  updated = db.DateTimeProperty(auto_now=True)
  navn = db.StringProperty(required=True)
  spaces = db.IntegerProperty(default=1)
  meldttilbage = db.BooleanProperty(default=False)
  vaerelse = db.BooleanProperty(default=False)
  betalt = db.BooleanProperty(default=False)
  type = db.StringProperty(required=True, default="Susanne",choices=['Susanne','S&oslash;ren','Venner'])

class Seng(db.Model):
  created = db.DateTimeProperty(auto_now_add=True)
  updated = db.DateTimeProperty(auto_now=True)
  double=db.IntegerProperty(required=True,default=18)
  single=db.IntegerProperty(required=True,default=4)

  @staticmethod
  def get():
    return Seng.get_or_insert("_the_single_")


