import djangoforms

from model import *

class GaestForm(djangoforms.ModelForm):
  class Meta:
    model = Gaest


class SengForm(djangoforms.ModelForm):
  class Meta:
    model = Seng

class WishForm(djangoforms.ModelForm):
    class Meta:
        model = Wish
