from django.shortcuts import render, redirect
from .models import City, Post, Profile
from django.contrib.auth.decorators import login_required
from .forms import Profile_Form, Post_Form
from django.contrib.auth.models import User


# Create your views here.
# ===== MAIN ===== #
def home(request): 
  context = {'title': 'Wayfarer'}
  return render(request, 'home.html', context)


# ===== AUTH  ======= #
# ===== IN ACCOUNTS APP


## ===== CITY ===== #
# city routes
@login_required
def city_show(request, city_id):
  city = City.objects.get(id = city_id)
  towns = City.objects.all()
  posts = city.post_set.all()
  post_form = Post_Form(request.POST)
  context = {'city': city, 'title': city.name, 'towns': towns, 'posts': posts, 'post_form': post_form }
  return render(request, 'cities/show.html', context)


# ===== POSTS ===== #
# post show
@login_required
def post_show(request, post_id):
  post = Post.objects.get(id = post_id)
  context = {'post': post, 'title': post.title}
  return render(request, 'posts/show.html', context)


# post new from main page
@login_required
def post_new(request):
  if request.method == 'POST':
    post_form = Post_Form(request.POST)
    if post_form.is_valid():
      new_post = post_form.save(commit=False)
      new_post.author = request.user.profile
      new_post.save()
      return redirect('profile_show', profile_id = request.user.profile.id)
  else:
    post_form = Post_Form()    
  return render(request, 'posts/new.html', { 'post_form': post_form })


# post edit
@login_required
def post_edit(request, post_id):
  post = Post.objects.get(id = post_id)
  if request.method == 'POST':
    if request.user.id == post.author.user.id:
      post_form = Post_Form(request.POST, instance=post)
      if post_form.is_valid():
        post_form.save()
        return redirect('post_show', post_id=post_id)
    else: 
      return redirect('post_show', post_id=post_id)
  else:
    post_form = Post_Form(instance = post)
  context = {'post': post, 'post_form': post_form, 'title': f"Edit {post.title}"}
  return render(request, 'posts/edit.html', context)


# post delete
@login_required
def post_delete(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.user.id == post.author.user.id:
    post.delete()
  return redirect('profile_show', profile_id = request.user.profile.id)




# ==== PROFILE ==== #
@login_required
def profile_show(request, profile_id): 
  profile = Profile.objects.get(id=profile_id)
  posts = profile.post_set.all()
  context = {'profile': profile, 'title': profile.name, 'posts': posts}
  return render(request, 'profile/show.html', context)

@login_required
def profile_edit(request, profile_id): 
  profile = Profile.objects.get(id=profile_id)
  if request.method == 'POST':
    if request.user.id == profile.user.id: 
      profile_form = Profile_Form(request.POST, instance=profile)
      if profile_form.is_valid(): 
        profile_form.save() 
        return redirect('profile_show', profile_id=profile_id)
    else:
      return redirect('profile_show', profile_id=profile_id)
  else: 
    profile_form = Profile_Form(instance=profile)
  context = {'profile': profile, 'profile_form': profile_form, 'title': profile.name }
  return render(request, 'profile/edit.html', context)

@login_required  
def profile_delete(request, user_id): 
  user = User.objects.get(id=user_id)
  if request.user.id == user.id:
    user.delete() 
  return redirect("/")

