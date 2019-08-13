from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='calculus-home'),
  path('about/', views.about, name='calculus-about'),
  path('problem-generator/', views.probgen, name='calculus-probgen'),
]
