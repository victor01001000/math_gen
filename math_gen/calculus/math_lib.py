#!/usr/bin/env python3
import random

# A library containing the math operators. For now, this file will contain all the common math operators. 

def add (var1, var2):
	return var1 + var2

def subtract(var1, var2): 
	return var1 - var2

def multiply(var1, var2):
	return var1 * var2

def divide(var1, var2):
	return var1 / var2

# Assume that user will enter any number but 0
# Returns a set of common factors
def find_common_factors(num):
	number = abs(num)
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
	numerator = num_den[0]
	denominator = num_den[1]
	gcf = find_greatest_common_factor(numerator, denominator)

	numerator = str(numerator / gcf)
	denominator = str(denominator / gcf)

	return numerator + "/" + denominator

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
def complex_polygen(number_of_terms, min_const=1, max_const=100, min_expo=1, max_expo=10):
  constants = []
  exponents = []
  problem=""
  for i in range(random.randint(1, number_of_terms)):
    constants.append(random.randint(min_const, max_const))
    exponents.append(random.randint(min_expo, max_expo))
  for i,j in zip(constants, exponents):
    problem += str(i)
    problem += 'x^'
    problem += str(j)
    problem += '+'
  problem = problem[:-1]
  return str(problem)

#################################################################################
#
#  Descrition: This method will separate the terms of a polynomial expression 
#    into an array
#
#  Params: polynomial expression
#
#  Returns an array of separate terms from the polynomial expression
#
#  Example:
#
#################################################################################
def separate_terms(problem):
  terms = problem.split('+')
  return terms

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
def power_rule(problem):
  terms = separate_terms(problem)
  constants = []
  powers = []
  new_constants = []
  new_powers = []
  answer = ""
  for i in terms:
    constants.append(i.split('x^', 1)[0])
    powers.append(i.split('x^', 1)[1])
  for i, j in zip(constants, powers):
    new_constants.append(int(i) * int(j))
  for i in powers:
    new_powers.append(int(i) - 1)
  for i,j in zip(new_constants, new_powers):
    answer += str(i)
    answer += 'x^'
    answer += str(j)
    answer += '+'
  answer = answer[:-1]
  return str(answer)

	
	
	
