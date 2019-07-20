#!/usr/bin/env python3
import sys
sys.path.insert(0, './')
from Variable import Variable
import random

class Polynomial:
    # initializer
    def __init__(self, eq_len, max_coeff, min_coeff, max_deg, min_deg, var_type):
        self.equation_length = eq_len
        self.max_coefficient = max_coeff
        self.min_coefficient = min_coeff
        self.max_degree = max_deg
        self.min_degree = min_deg
        self.variable_letter = var_type

    # methods
    def __generate_variable__(self):
        coefficient = random.randint(self.min_coefficient, self.max_coefficient)
        degree = random.randint(self.min_degree, self.max_degree)

        return Variable(coefficient, self.variable_letter, degree)

    def __generate_variable_deg__(self, degree):
        coefficient = random.randint(self.min_coefficient, self.max_coefficient)

        return Variable(coefficient, self.variable_letter, degree)

    def __generate_equation__(self, var_list):
        equation = ""
        for index in range(len(var_list)):
            var = var_list[index]
            if(index == 0):
                equation = equation + var.get_function()
            else:
                if(var.get_coefficient() < 0):
                    equation = equation + var.get_function()
                else:
                    equation = equation + "+" + var.get_function()

        return equation


    def get_equation_sequential(self):
        variable_list = list()

        degree = self.max_degree
        while(degree >= self.min_degree):
            coefficient = random.randint(self.min_coefficient, self.max_coefficient)
            var = Variable(coefficient, self.variable_letter, degree)

            variable_list.append(var)

            degree = degree - 1

        return self.__generate_equation__(variable_list)

poly = Polynomial(3, 3, 1, 2, 0, "x")
print(poly.get_equation_sequential())




