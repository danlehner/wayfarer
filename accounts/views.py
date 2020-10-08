from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def signup(request): 
  if request.method == "POST": 
    name = request.POST['name']
    current_city = request.POST['current_city']
    date_joined = request.POST['date_joined']
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
          password=password,
          name=name,
          current_city=current_city,
          date_joined=date_joined)
        user.save() 
  return render(request, 'signup.html')

