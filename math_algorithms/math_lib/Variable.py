#!/usr/bin/env python3

class Variable:
	# intializer

	"""
	@ param: coefficient, variable type, degree
	"""
	def __init__(self, coeff, var, power):
		self.coefficient = str(coeff)
		self.variable = str(var)
		self.degree = str(power)
	
	"""
	Method to return whole function.
	@ return: ax^b
	"""
	def get_function(self):
		if(int(self.degree) == 0):
			return self.coefficient

		elif(int(self.coefficient) == 1):
			return self.variable + "^" + self.degree

		return self.coefficient + self.variable + "^" + self.degree

	"""
	Method to return coefficient of the variable.
	@ return: a
	"""
	def get_coefficient(self):
		return int(self.coefficient)

	"""
	Method to retrieve variable type.
	@ return x
	"""
	def get_variable(self):
		return self.variable

	"""
	Method to retrieve the degree of function
	@ return b
	"""
	def get_degree(self):
		return int(self.degree)
