#!/usr/bin/env python3
  
import sys
sys.path.insert(0, './math_lib')
import Polynomial
import unittest

class PolynomialTests(unittest.TestCase):

poly = Polynomial.Polynomial(1, 5, -3, 10, 2, 8, 'x')

print(poly)
  
if __name__ == '__main__':
  unittest.main()
  
