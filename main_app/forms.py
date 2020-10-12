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

<<<<<<< HEAD
class Comment_Form(ModelForm): 
  class Meta: 
    model = Comment
    fields = ['text']
    
=======
class Post_Form_Modal(ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'text']
>>>>>>> 6a6a791fc4d81e403e705f20ef1f5cc4f2ef1f38
