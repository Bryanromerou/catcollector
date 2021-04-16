from django import forms
from .models import Feeding, Cat, Profile
from pyuploadcare.dj.forms import ImageField

class FeedingForm(forms.ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']

class CatForm(forms.ModelForm):
  class Meta:
    model = Cat
    fields = ['name','age','breed','description']

class ProfileForm(forms.ModelForm):
  profile_pic = ImageField(label='Profile Picture')

  class Meta:
    model = Profile
    fields = ("name","profile_pic",)

class ProfileForm2(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ("name","email",)