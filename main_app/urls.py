from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('cities/<int:city_id>/', views.city_show, name='city_show')
]