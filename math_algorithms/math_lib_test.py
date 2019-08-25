#!/usr/bin/env python3

import sys
sys.path.insert(0, './math_lib')
import math_lib
import unittest

class MathGenTests(unittest.TestCase):

  # Verifies power rule method is working
  def test_power_rule(self):
    print('Power rule')
    self.assertEqual(math_lib.power_rule('5x^2'), '10x^1')
 
  # Verifies reduce fraction method is working
  def test_reduce_fraction(self):
    print('Reduce Fractions')
    self.assertEqual(math_lib.reduce_fraction('4/8'), '1.0/2.0')

  # Verfies combined like terms method is working 

  # Verifies separate_constants_exponents is working

  # Verifies multiplying two polynomials works
  def test_multiply_polynomial(self):
    print('Multiplying polynomials')
    self.assertEqual(math_lib.multiply_polynomials('5x+1', '2x^2+5'), '10x^3+2x^2+25x^1+5x^0')

if __name__ == '__main__':
  unittest.main()

