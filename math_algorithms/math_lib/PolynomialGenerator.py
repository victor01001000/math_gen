#!/usr/bin/env python3

import Variable
import random


# this could be PolynomialGenerator and the equations generated get stored in Polynomial.

class PolynomialGenerator():

    def __init__(self, length, letter):
        self.eq_length = length
        self.var_letter = letter

        self.terms_list = list()

    def are_there_like_terms(self):
        for i in range(len(self.terms_list)):
            current_term = self.terms_list[i]

            for j in range(i + 1, len(self.terms_list)):
                maybe_like_term = self.terms[j]

                if current_term.var_letter == maybe_like_term.var_letter:
                    if current_term.degree == maybe_like_term.degree:
                        return True
        return False


    def add_like_terms(self):
        new_equation = list()

        for i in range(len(self.terms_list)):
            current_term = self.terms_list[i]

            for j in range(i + 1, len(self.terms_list)):
                next_term = self.terms_list[j]

                same_var_letters = current_term.var_letter == next_term.var_letter
                same_degree = current_term.degree == next_term.degree

                if same_var_letters and same_degree:
                    combined_coeff = str(int(current_term.coefficient + next_term.coefficient))

                    new_equation.append(Variable(combined_coeff, current_term.var_letter, current_term.degree))

                    new_equation.remove(current_term)
                    new_equation.remove(next_term)

            new_equation.append(current_term)

        self.terms_list = new_equation


    def generate_equation_sequential(self, min_coeff, max_coeff, min_deg):
        current_deg = min_deg
        max_deg = min_deg + self.eq_length
        while current_deg <= max_deg:
            coefficient = random.randint(min_coeff, max_coeff)
            var = Variable(coefficient, self.var_letter, current_deg)

            self.terms_list.append(var)

            current_deg = current_deg + 1


    def generate_equation_random(self, min_coeff, max_coeff, min_deg, max_deg):
        i = 0
        while i < self.eq_length:
            degree = random.randint(min_deg, max_deg)
            coefficient = random.randint(min_coeff, max_coeff)
            self.terms_list.append(Variable(coefficient, self.var_letter, degree))

            if self.are_there_like_terms():
                self.add_like_terms()

                i = len(self.terms_list)

            i = i + 1
