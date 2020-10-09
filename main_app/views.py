from django.shortcuts import render, redirect
from .models import City, Post, Profile
from .forms import Profile_Form, Post_Form

# Create your views here.
# ===== MAIN ===== #
def home(request): 
  context = {'title': 'Wayfarer'}
  return render(request, 'home.html', context)


# ===== AUTH  ======= #
# ===== IN ACCOUNTS APP


## ===== CITY ===== #
# city routes
def city_show(request, city_id):
  city = City.objects.get(id = city_id)
  towns = City.objects.all()
  posts = city.post_set.all()
  context = {'city': city, 'title': city.name, 'towns': towns, 'posts': posts}
  return render(request, 'cities/show.html', context)


# ===== POSTS ===== #
# post show
def post_show(request, post_id):
  post = Post.objects.get(id = post_id)
  context = {'post': post, 'title': post.title}
  return render(request, 'posts/show.html', context)


# post edit
def post_edit(request, post_id):
  post = Post.objects.get(id = post_id)
  if request.method == 'POST':
    post_form = Post_Form(request.POST, instance=post)
    if post_form.is_valid():
      post_form.save()
      return redirect('post_show', post_id=post_id)
  else:
    post_form = Post_Form(instance = post)
  context = {'post': post, 'post_form': post_form, 'title': f"Edit {post.title}"}
  return render(request, 'posts/edit.html', context)


# post delete
def post_delete(request, post_id):
  pass

# ==== PROFILE ==== #
def profile_show(request, profile_id): 
  profile = Profile.objects.get(id=profile_id)
  posts = profile.post_set.all()
  context = {'profile': profile, 'title': profile.name, 'posts': posts}
  return render(request, 'profile/show.html', context)


def profile_edit(request, profile_id): 
  profile = Profile.objects.get(id=profile_id)
  if request.method == 'POST': 
    profile_form = Profile_Form(instance=profile)

  