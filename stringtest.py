#! /usr/bin/python

import unittest

class TestBasicString(unittest.TestCase):

    testString = "APRIL is the cruellest month, breeding"

    def test_concat(self):
        result = "Tonle " + "Sap"
        self.assertEqual(result, "Tonle Sap")

    def test_repeat(self):
        result = "Ha" * 5 + "!"
        self.assertEqual(result, "HaHaHaHaHa!")

    def test_slice(self):
        self.assertEqual(TestBasicString.testString[4], 'L')
        self.assertEqual(TestBasicString.testString[:5], "APRIL")
        self.assertEqual(TestBasicString.testString[6:], "is the cruellest month, breeding")
        self.assertEqual(TestBasicString.testString[13:22], "cruellest")

if __name__ == '__main__':
    unittest.main()
