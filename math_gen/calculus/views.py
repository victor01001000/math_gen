from django.shortcuts import render
from django.http import HttpResponse

# Loads html file for home page
def home(request):
  return render(request, 'calculus/home.html')

def about(request):
  return HttpResponse('<h1>About</h1>')

def probgen(request):
  return HttpResponse('<h1>Problem Generator</h1>')
