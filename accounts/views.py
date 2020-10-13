from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from main_app.models import Profile
from wayfarer_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

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
        email = user.email
        return redirect(f'/accounts/send_email/{email}')
  return render(request, 'signup.html')

def send_email(request, email):
  subject = 'Meet the Wayfarer Team'
  message = 'Wayfarer is a tech demo constructed by in less than a week by a three person team new to its underlying technologies: Django, Postgres SQL Database, and Semantic-UI.\n\n If you like what you see maybe, you would like to work with one or all of us.\n\n Jeffrey Thompson - jeffathomp@gmail.com\n Dan Lehner - LehnerDR@gmail.com\n Jason Andersen - andersen.ja@gmail.com\n\n Sincerely,\n The Wayfarer Team'  
  recipient = email
  send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
  return redirect('/accounts/login')

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


