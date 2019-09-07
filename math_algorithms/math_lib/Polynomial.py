#!/usr/bin/env python3

class Polynomial():
  
  """
  Initializer has default parameters and can be changed. 
  
  Parameters: 
  -length of equation is a random number between min_terms and max_terms. 
  -parameters for constants have to be positve. 
  -parameters for degree can be negative or positive. 
  -equation is one type of variable letter. 
  """
  def __init__(self, min_terms = 1, max_terms = 5, min_const = 1, max_const = 5, min_deg = 0, max_deg = 6, letter = 'x'):
    self.terms_list = list()
   
    for i in range(random.randint(min_terms, max_terms)):
      signs = ['+', '-']
      self.terms_list.append(
       {
         'sign': signs[random.randint(0, 1)]
         'constant': random.randint(min_const, max_const),
         'variable': letter, 
         'exponent': random.randint(min_deg, max_deg),
       }
      )
  
  def __repr__(self):
    equation = ''
    
    for i in range(len(self.terms_list)):
      gx = self.terms_list[i]
      equation += gx['signs'] + gx['constant'] + gx['variable'] + '^' + gx['exponent']
      
    return equation
  
  def get_derivative(self):
    problem_array = self.terms_list
    
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

#   def generate_equation_sequential(self, min_coeff, max_coeff, min_deg):
   
#     current_deg = min_deg
#     max_deg = start_deg + self.eq_length
#     while current_deg <= max_deg:
#       coefficient = random.randint(min_coeff, max_coeff)
#       var = Variable(coefficient, self.var_letter, current_deg)  
      
#       self.terms_list.append(var)

#       current_deg = current_deg + 1

#   def generate_equation_random(self, min_coeff, max_coeff, min_deg, max_deg):
#     pass
