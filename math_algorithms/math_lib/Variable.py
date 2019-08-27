#!/usr/bin/env python3

class Variable:
    # intializer

    """
    @ param: coefficient, variable type, degree
    """

    def __init__(self, coeff, letter, power):
        self.coefficient = str(coeff)
        self.var_letter = str(letter)
        self.degree = str(power)

    """
    Method to return whole function.
    @ return: ax^b
    """

    def get_function(self):
        if (int(self.degree) == 0):
            return self.coefficient

        elif (int(self.coefficient) == 1):
            return self.variable + "^" + self.degree

        return self.coefficient + self.variable + "^" + self.degree