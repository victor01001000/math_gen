#!/usr/bin/env python3
import random
import re
import math

# A library containing the math operators. For now, this file will contain all the common math operators. 
 

# Assume that user will enter any number but 0
# Returns a set of common factors
def find_common_factors(num):
	number = abs(int(num))
	common_factors = set()

	possible_factors = 1
	while (possible_factors <= number):
		if (number % possible_factors == 0):
			common_factors.add(possible_factors)

		possible_factors = possible_factors + 1

	return common_factors


# Returns the GCF between two numbers
def find_greatest_common_factor(num1, num2):
	num1_common_factors = find_common_factors(num1)
	num2_common_factors = find_common_factors(num2)

	common_factors = num1_common_factors.intersection(num2_common_factors)
	
	greatest_common_factor = max(common_factors)

	return greatest_common_factor

# Assume that user will enter fraction as num1/num2
# This method could be organized in a fraction class 
def reduce_fraction(fraction):
	num_den = fraction.split('/')
	numerator = int(num_den[0])
	denominator = int(num_den[1])
	gcf = find_greatest_common_factor(numerator, denominator)

	numerator = numerator / gcf
	denominator = denominator / gcf

	return str(numerator) + '/' + str(denominator)

#################################################################################
#
#  Descrition: This method will generate a simple polynomial expression with
#    two terms. The minimum and maximum values are set at 1 to 100 for the 
#    constants and 1 to 10 for the exponents.
#
#  Returns simple polynomial with two expressions
#
#  Example:
#
#################################################################################
def simple_polygen():
  return str(random.randint(1,100)) + 'x^' + str(random.randint(1,10)) + '+' + str(random.randint(1,100)) + 'x^' + str(random.randint(1,10))
  

#################################################################################
#
#  Descrition: This method will generate a complex polynomial expression based
#    off of user input
#
#  Params: number of terms, minimum/maximum constant, minimum/maximum exponent
#
#  Returns a string of a complex polynomial expression
#
#  Example:
#
#################################################################################
def complex_polygen(min_terms=1, max_terms=5, min_const=1, max_const=100, min_expo=1, max_expo=10, variables=1):
  problem_array = []
  signs = ['+', '-']
  problem=""
  for i in range(random.randint(min_terms, max_terms)):
    problem_array.append(
      {
        'sign': signs[random.randint(0,1)],
        'constant': random.randint(min_const, max_const),
        'exponent': random.randint(min_expo, max_expo),
        'variable': 'x'
      }
    )
  return problem_array

def formulate_problem(problem_array):
  problem_string=''
  for i in problem_array:
    problem_string += f"{i['sign']}{i['constant']}{i['variable']}^{i['exponent']}"
  if problem_string[0] == '+':
    return problem_string[1:]
  else:
    return problem_string

#################################################################################
#
#  Descrition: This method will parse inputted polynomial
#
#  Params: polynomial expression
#
#  Returns a dictionary of different parts of the polynomial
#
#  Example:
#
#################################################################################
def parse_problem(problem):
  problem_dict = []
  terms = re.split('\+|\-', problem)
  variables = []
  for a in terms:
    if re.match('^.*[a-z].*$', a):
      variables.append(re.findall('[a-z]', a)[0])
    else:
      variables.append('None')
  signs = re.findall('\+|\-', problem)
  if problem[0] != '-':
    signs.insert(0, '+')
  for a, i, j, k in zip(range(len(terms)), terms, variables, signs):
    problem_dict.append({
      'sign': k,
      'constant': 1 if i.split(j)[0] == '' else int(i.split(j)[0]), 
      'variable': j,
      'exponent': int(0 if j not in i else (i.split(f"{j}^")[1] if f"{j}^" in i else 1))
    })
  return problem_dict

#################################################################################
#
#  Descrition: This method will solve and return a solution for an inputted 
#    polynomial expression. The input should be of type string. 
#  
#  Format of Input: kx^e
#    k - constant
#    x - variable
#    e - exponent
#
#  Returns the derivative of the inputted problem
#
#  Example:
#
#################################################################################
def power_rule(problem_array):
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

#################################################################################
#
# Descrition: This method will multiply two polynomials
#
# Params: Two polynomials (Will accept more in the future)
#
#################################################################################
def multiply_polynomials(poly1, poly2):
  terms_poly1 = parse_problem(poly1)
  terms_poly2 = parse_problem(poly2)
  answer = ''
  answer_constants = []
  answer_exponents = []
  new_signs = []
  for i in range(len(terms_poly1)):
    for j in range(len(terms_poly2)):
      answer_constants.append(terms_poly1[j]['constant'] * terms_poly2[i]['constant'])
      answer_exponents.append(terms_poly1[j]['exponent'] + terms_poly2[i]['exponent'])
      if terms_poly1[j]['sign'] == terms_poly2[i]['sign']:
        new_signs.append('+')
      else:
        new_signs.append('-')
  for a, b, c in zip(answer_constants, answer_exponents, new_signs):
    answer += f"{str(a)}x^{str(b)}{str(c)}"
  return answer[:-1]

#################################################################################
#
# Descrition: Product rule
#
# Params:
#
#################################################################################
def product_rule(problem):
  terms = []
  derived_terms = []
  a = re.findall('\(.*?\)',problem)
  for i in a:
    terms.append(i.strip('(').strip(')'))
  for x in terms:
    derived_terms.append(power_rule(x))
  answer = derived_terms
  new_problem = str(terms[0] + ' ' + str(derived_terms[1]))
  return new_problem, answer


# Assume problem is poly1/poly2
def quotient_rule(problem):
  pass
  
