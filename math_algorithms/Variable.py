class Variable:
	# intializer 
	# @param: coefficient, power, variable 
	def __init__(self, coeff, power, var):
		self.coefficient = str(coeff)
		self.degree = str(power)
		self.variable = var
	
	# Returns ax^b
	def get_variable(self):
		if(self.degree == 0):
			return self.coefficient
		return self.coefficient + self.variable + "^" + self.degree

	def get_coefficient(self):
		return int(self.coefficient)

	def get_degree(self):
		return int(self.degree)
