from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinLengthValidator


# Create your models here.

class Profile(models.Model): 
  name = models.CharField(max_length=50)
  current_city = models.CharField(max_length=50)
  date_joined = models.DateField(auto_now=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.URLField('link to a picture of you', default='https://res.cloudinary.com/dvk80uh1a/image/upload/v1602285072/u9acqxd8itejhuqp0pai.jpg')

  def __str__(self): 
    return self.name


class City(models.Model): 
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=150)

  def __str__(self): 
    return self.name

class Post(models.Model): 
  title = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
  text = models.TextField()
  date_created = models.DateTimeField(auto_now=True)

  author = models.ForeignKey(Profile, on_delete=models.CASCADE)
  city = models.ForeignKey(City, on_delete=models.CASCADE)

  def __str__(self): 
    return self.title

  class Meta: 
    ordering = ['-date_created']

class Comment(models.Model): 
  text = models.TextField()
  date_commented = models.DateTimeField(auto_now=True)

  commenter = models.ForeignKey(Profile, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)

  class Meta: 
    ordering = ['-date_created']

