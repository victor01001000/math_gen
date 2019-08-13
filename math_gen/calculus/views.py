from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Home</h1>')

def about(request):
  return HttpResponse('<h1>About</h1>')

def probgen(request):
  return HttpResponse('<h1>Problem Generator</h1>')
