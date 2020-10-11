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
    image = request.POST['image']

    if image:
      image = image
    else:
      image = 'https://res.cloudinary.com/dvk80uh1a/image/upload/v1602285072/u9acqxd8itejhuqp0pai.jpg'
    if User.objects.filter(username=username_form).exists():
      context = {'error': 'Username is already taken'}
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
        profile = Profile(current_city=current_city, name=name, user=user, image=image)
        profile.save()
        return redirect('/accounts/login')
  return render(request, 'signup.html')

def login(request): 
    if request.method == 'POST': 
      username_form = request.POST['username']
      password_form = request.POST['password']
      user = auth.authenticate(username=username_form, password=password_form)
      if user is not None: 
        auth.login(request, user)
        return redirect('profile_show', profile_id = user.profile.id)
      else: 
        context = {'error': 'Invalid credentials'}
        return render(request, 'login.html', context)
    else: 
      return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


