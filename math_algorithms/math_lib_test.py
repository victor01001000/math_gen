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

  # Verfies combined like terms method is working 

  # Verifies random polynomial is being generated

  # Verifies separate_constants_exponents is working

#print(math_lib.read_and_formulate_problem('5x+6x^2-7y^10+7'))

print(math_lib.multiply_polynomials('5x+1', '2x^2+5'))

if __name__ == '__main__':
  unittest.main()

