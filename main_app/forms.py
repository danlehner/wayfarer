from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import City, Profile, Post, Comment

class Profile_Form(ModelForm):
  class Meta: 
    model = Profile
    fields = ['name', 'current_city', 'image']

class Post_Form(ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'text', 'city']

class Comment_Form(ModelForm): 
  class Meta: 
    model = Comment
    fields = ['text']
    