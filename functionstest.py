#! /usr/bin/python

import random
import unittest

def factorial(n): # return the n! factorial
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

class TestSequenceFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(120, factorial(5))

if __name__ == '__main__':
    unittest.main()
