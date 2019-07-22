#!/usr/bin/env python3
import sys

sys.path.insert(0, './')
from Variable import Variable
import random

class Polynomial:
    # initializer
    def __init__(self, eq_len, letter):
        self.eq_length = eq_len
        self.var_letter = letter

        self.var_list = list()


# methods
    def generate_equation_random(self, max_coeff, min_coeff, max_deg, min_deg):
        num_vars = 0

        while num_vars < self.eq_length:
            coefficient = random.randint(min_coeff, max_coeff)
            degree = random.randint(min_deg, max_deg)

            self.var_list.append(Variable(coefficient, self.var_letter, degree))

            num_vars = num_vars + 1

    def generate_equation_sequential(self, max_coeff, min_coeff, max_deg):
        num_vars = 0

        while num_vars < self.eq_length:
            coefficient = random.randint(min_coeff, max_coeff)
            degree = max_deg - num_vars

            self.var_list.append(Variable(coefficient, self.var_letter, degree))

            num_vars = num_vars + 1


    def get_equation(self):
        equation = self.var_list[0].get_function()

        index = 1
        while index < self.eq_length:
            var = self.var_list[index]

            if var.get_coefficient() < 0:
                equation += var.get_function()
            else:
                equation += "+" + var.get_function()

            index = index + 1

        return equation


    def get_variable_list(self):
        return self.var_list
