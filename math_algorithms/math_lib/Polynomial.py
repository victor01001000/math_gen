#!/usr/bin/env python3
import random


class Polynomial():
    """
    Description:
    A polynomial is described as a list of monomials.

    The initializer's default parameter is an empty list of monomials; however, it it has
    defualt parameters to generating a random equation.

    """
    def __init__(self, terms_list=list()):
        self.equation = terms_list

        if len(self.equation) is 0:
            self.equation = list()

            # Default parameters for a random equation
            min_terms = 1
            max_terms = 5
            min_const = 1
            max_const = 10
            min_deg = 1
            max_deg = 7

            self.equation = self.generate_random_equation(min_terms, max_terms, min_const, max_const, min_deg, max_deg)

    def __repr__(self):
        return self.get_equation()

    """
    Description: 
    Generates a random polynomial equation based on the parameters given. 
    
    Parameters:
    -length of equation is a random number between min_terms and max_terms.
    -parameters for constants-- min_const and max_const-- have to be positive.
    -parameters for degree can be negative or positive.
    -equation is one type of variable letter.
        
    Returns: 
    void
        
    """
    def generate_random_equation(self, min_terms, max_terms, min_const, max_const, min_deg, max_deg, letter):
        new_equation = list()

        signs = ['+', '-']
        for i in range(random.randint(min_terms, max_terms)):
            new_equation.append(
                {
                    'sign': signs[random.randint(0, 1)],
                    'constant': random.randint(min_const, max_const),
                    'variable': letter,
                    'exponent': random.randint(min_deg, max_deg),
                }
            )

        self.terms_list = new_equation

    """
    Description: 
    Generates and returns the first derivative of the equation.
      
    Parameters:
    none
      
    Returns: 
    A list of dictionaries that define a monomial. 
    """
    def get_derivative(self):
        function = self.equation

        function_prime = []
        for i in range(len(function)):
            function_prime.append(
                {
                    'sign': function[i]['sign'],
                    'constant': function[i]['constant'] * function[i]['exponent'],
                    'exponent': function[i]['exponent'] - 1,
                    'variable': function[i]['variable']
                }
            )
        return function_prime

    """
        Description: 
        Constructs a string that represents the equation based on the terms inside self.equation list. 
        
        Parameters:
        None
        
        Returns: 
        The equation constructed in a string. 
    """
    def get_equation(self):
        equation = ''

        for i in range(len(self.equation)):
            gx = self.equation[i]
            if (gx['sign'] is '+') and (i == 0):
                equation += str(gx['constant']) + gx['variable'] + '^' + str(gx['exponent'])
            else:
                equation += gx['sign'] + str(gx['constant']) + gx['variable'] + '^' + str(gx['exponent'])

        return equation
