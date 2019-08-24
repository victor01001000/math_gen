#!/usr/bin/env python3

import sys
sys.path.insert(0, './math_lib')
import math_lib
import unittest

class MathGenTests(unittest.TestCase):

  # Verifies power rule method is working
  def test_power_rule(self):
    self.assertEqual(math_lib.power_rule('5x^2'), '10x^1')
 
  # Verifies reduce fraction method is working
  def test_reduce_fraction(self):
    self.assertEqual(math_lib.reduce_fraction('4/8'), '1/2')

  # Verfies combined like terms method is working 

  # Verifies random polynomial is being generated

print(math_lib.simple_polygen())

print(math_lib.complex_polygen(5))


if __name__ == '__main__':
  unittest.main()

