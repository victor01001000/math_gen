#!/usr/bin/env python3

import sys
sys.path.insert(0, './')
import math_lib
import unittest

class MathGenTests(unittest.TestCase):

  # Verifies power rule method is working
  def test_power_rule(self):
    self.assertEqual(math_lib.power_rule('5x^2'), '10x^1')
  

print(math_lib.simple_polygen())

print(math_lib.complex_polygen(5))


if __name__ == '__main__':
  unittest.main()

