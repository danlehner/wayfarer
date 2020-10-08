from django.shortcuts import render, redirect
from .models import City, Post

# Create your views here.

def home(request): 
  context = {'title': 'Wayfarer'}
  return render(request, 'home.html', context)

# city routes
def city_show(request , city_id):
  city = City.objects.get(id = city_id)
  towns = City.objects.all()
  posts = city.post_set.all()
  context = {'city': city, 'title': city.name, 'towns': towns, 'posts': posts}
  return render(request, 'cities/show.html', context)
