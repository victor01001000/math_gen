#!/usr/bin/env python3
from django.shortcuts import render
from django.http import HttpResponse
import random
import sys
from . import math_lib


# Loads html file for home page
def home(request):
  polynomial = math_lib.complex_polygen(1)
  problem = {
    'problem': polynomial,
    'answer' : math_lib.power_rule(polynomial)
  }
  return render(request, 'calculus/home.html', problem)

def about(request):
  return HttpResponse('<h1>About</h1>')

def probgen(request):
  return HttpResponse('<h1>Problem Generator</h1>')
