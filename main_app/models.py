from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model): 
  name = models.CharField(max_length=50)
  current_city = models.CharField(max_length=50)
  date_joined = models.DateField(auto_now=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self): 
    return self.name

class City(models.Model): 
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=150)

  def __str__(self): 
    return self.name

class Post(models.Model): 
  title = models.CharField(max_length=100)
  text = models.TextField()
  date_created = models.DateTimeField(auto_now=True)

  author = models.ForeignKey(Profile, on_delete=models.CASCADE)
  city = models.ForeignKey(City, on_delete=models.CASCADE)

  def __str__(self): 
    return self.title

  class Meta: 
    ordering = ['-date_created']

