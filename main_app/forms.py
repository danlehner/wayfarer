from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import City, Profile, Post

class Profile_Form(ModelForm):
  class Meta: 
    model = Profile
    fields = ['name', 'current_city']