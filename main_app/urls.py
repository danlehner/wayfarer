from django.urls import path
from . import views

urlpatterns = [
  # ===== MAIN ===== #
  path('', views.home, name='home'),

  # ===== CITY ===== #
  path('cities/<int:city_id>/', views.city_show, name='city_show'),

  # ===== POST ===== #
  path('posts/new/', views.post_new, name="post_new"),
  # path('posts/<int:city_id>/new_from_city/', views.post_new_from_city, name="post_new_from_city"),
  path('posts/<int:post_id>/', views.post_show, name='post_show'),
  path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
  path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),

  # ==== PROFILE ==== #
  path('profile/<int:profile_id>/', views.profile_show, name='profile_show'),
  path('profile/<int:profile_id>/edit', views.profile_edit, name='profile_edit'), 
  path('profile/<int:user_id>/delete', views.profile_delete, name='profile_delete')
]