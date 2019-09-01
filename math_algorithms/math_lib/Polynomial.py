#!/usr/bin/env python3

import Variable 
import random

# this could be PolynomialGenerator and the equations generated get stored in Polynomial. 

class Polynomial():

  def __init__(self, min_terms, max_terms, min_const, max_const, min_deg, max_deg, letter):
    self.terms_list = list()
   
    for i in range(random.randint(min_terms, max_terms)):
      self.terms_list.append(
       {
         'constant': random.randint(min_const, max_const),
         'exponent': random.randint(min_deg, max_deg),
         'variable': letter
       }
      )
  
  def __repr__(self):
    equation = ''
    
    for i in range(len(self.terms_list)):
      function = self.terms_list[i]
      if not (function['constant'] < 0):
        equation += '+' + str(function['constant']) + function['variable'] + '^' + str(function['exponent']) 
      
    return equation
  
  def get_derivative(self):
    answer_array = []
    for i in range(len(problem_array)):
      answer_array.append(
        {
          'sign': problem_array[i]['sign'],
          'constant': problem_array[i]['constant'] * problem_array[i]['exponent'],
          'exponent': problem_array[i]['exponent'] - 1,
          'variable': problem_array[i]['variable']
        }
      )
    return answer_array

  def generate_equation_sequential(self, min_coeff, max_coeff, min_deg):
   
    current_deg = min_deg
    max_deg = start_deg + self.eq_length
    while current_deg <= max_deg:
      coefficient = random.randint(min_coeff, max_coeff)
      var = Variable(coefficient, self.var_letter, current_deg)  
      
      self.terms_list.append(var)

      current_deg = current_deg + 1


  def generate_equation_random(self, min_coeff, max_coeff, min_deg, max_deg):
    pass  

