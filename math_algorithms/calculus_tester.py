#!/usr/bin/env python3

import sys

sys.path.insert(0, './math_lib')
import Polynomial
import random
import unittest


class PolynomialTests(unittest.TestCase):

    def test_get_derivative(self):
        print('Finding derivative of x^2 + 3x^1')
        default_terms = []
        default_terms.append(
            {
                'sign': '+',
                'constant': 1,
                'variable': 'x',
                'exponent': 2,
            }
        )

        default_terms.append(
          {
            'sign': '-',
            'constant': 3,
            'variable': 'x',
            'exponent': 1,
          }
        )
        
        function = Polynomial(default_terms)
        function_prime = Polynomial(function.get_derivative())

        self.assertEqual(function_prime, '2x^1-3x^0')
        
        


if __name__ == '__main__':
    unittest.main()
