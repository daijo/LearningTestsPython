#! /usr/bin/python

import unittest

class TestBasicCalculations(unittest.TestCase):

    def test_subtraction(self):
        result = 2 - 1
        self.assertEqual(result, 1)

    def test_addition(self):
        result = 1 + 1
        self.assertEqual(result, 2)

    def test_imaginary(self):
        img = 2.0+4.0j
        self.assertEqual(img.real, 2)
        self.assertEqual(img.imag, 4)

if __name__ == '__main__':
    unittest.main()
