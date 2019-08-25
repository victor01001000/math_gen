#!/usr/bin/env python3

import sys
sys.path.insert(0, './math_lib')
import math_lib
import unittest

class MathGenTests(unittest.TestCase):

  def test_power_rule(self):
    print('Power rule')
    self.assertEqual(math_lib.power_rule('5x^2'), '10x^1')
 
  def test_reduce_fraction(self):
    print('Reduce Fractions')
    self.assertEqual(math_lib.reduce_fraction('4/8'), '1.0/2.0')

  def test_power_rule(self):
   print('Power Rule')
   self.assertEqual(math_lib.power_rule('x^2'), '2x')

  def test_multiply_polynomial(self):
    print('Multiplying polynomials')
    self.assertEqual(math_lib.multiply_polynomials('5x+1', '2x^2+5'), '10x^3+2x^2+25x^1+5x^0')

if __name__ == '__main__':
  unittest.main()

