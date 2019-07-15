#!/usr/bin/env python3

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
def find_greatest_common_factors(num1, num2):
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





	
	
	
