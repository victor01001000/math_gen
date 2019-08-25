#!/usr/bin/env python3
from django.shortcuts import render
from django.http import HttpResponse
import random
import sys
from . import math_lib


# Loads html file for home page
def home(request):
  problems = []
  problem_dict = {}
  for i in range(10):
    problems.append(math_lib.complex_polygen())
    problem_dict.update({f"problem{i}": problems[i]})
    problem_dict.update({f"answer{i}": math_lib.power_rule(problems[i])})
  return render(request, 'calculus/home.html', problem_dict)

def about(request):
  return HttpResponse('<h1>About</h1>')

def probgen(request):
  return HttpResponse('<h1>Problem Generator</h1>')
