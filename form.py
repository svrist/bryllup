from google.appengine.ext.db import djangoforms

from model import *

class GaestForm(djangoforms.ModelForm):
  class Meta:
    model = Gaest