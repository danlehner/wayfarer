from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from main_app.models import Profile

# Create your views here.

def signup(request): 
  if request.method == "POST": 
    name = request.POST['name']
    current_city = request.POST['current_city']
    username_form = request.POST['username']
    email_form = request.POST['email']
    password = request.POST['password']

    if User.objects.filter(username=username_form).exists():
      context = {'error': 'Usernane is already taken'}
      return render(request, 'signup.html', context)
    else: 
      if User.objects.filter(email=email_form).exists(): 
        context = {'error': 'Email already exists'}
        return render(request, 'signup.html', context)
      else: 
        user = User.objects.create_user(
          username=username_form,
          email=email_form,
          password=password)
        user.save() 
        profile = Profile(current_city=current_city, name=name, user=user)
        profile.save()
        return redirect('/')
  return render(request, 'signup.html')

