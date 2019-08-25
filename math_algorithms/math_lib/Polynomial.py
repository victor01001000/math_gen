#!/usr/bin/env python3

import Variable 
import random

class Polynomial():

  def __init__(self, length, letter):
    self.eq_length = length 
    self.var_letter = var_letter

    self.terms_list = list()

  def __assemble_equation__(self):
    equation = ''

    for i in range(self.eq_length):
      var = self,terms_list[i]
      
      if(var.get_coefficient() < 0):
        equation += '-' + var.get_function()
      else: 
	equation += '+' + var.get_fucntion()

     return equation
    	  
  def get_equation_sequential(self, min_coeff, max_coeff, min_deg):
   
    current_deg = min_deg
    max_deg = start_deg + self.eq_length
    while current_deg <= max_deg:
      coefficient = random.randint(min_coeff, max_coeff)
      var = Variable(coefficient, self.var_letter, current_deg)  
      
      self,terms_list.append(var)

      current_deg = current_deg + 1

    return self.__assemble_equation__()

  def get_equation_random(self, min_coeff, max_coeff, min_deg, max_deg);
    pass  
