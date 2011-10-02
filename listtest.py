#! /usr/bin/python

import unittest

class TestBasicString(unittest.TestCase):

    testList = ["APRIL", "is", "the", "cruellest", "month,", "breeding"]

    def test_concat(self):
        result = ["Bagel"] + ["Croissant"]
        self.assertEqual(result, ["Bagel", "Croissant"])

    def test_repeat(self):
        result =  ["Bagel", "Croissant"] * 2
        self.assertEqual(result, ["Bagel", "Croissant", "Bagel", "Croissant"])

    def test_slice(self):
        self.assertEqual(TestBasicString.testList[3], "cruellest")
        self.assertEqual(TestBasicString.testList[:2], ["APRIL", "is"])
        self.assertEqual(TestBasicString.testList[4:], ["month,", "breeding"])
        self.assertEqual(TestBasicString.testList[2:4], ["the", "cruellest"])

    def test_slice_negative(self):
        self.assertEqual(TestBasicString.testList[-4], "the")
        self.assertEqual(TestBasicString.testList[-2:],  ["month,", "breeding"])
        self.assertEqual(TestBasicString.testList[:-3], ["APRIL", "is", "the"])

    def test_slice_invariant(self):
        self.assertEqual(TestBasicString.testList[:3] + TestBasicString.testList[3:], TestBasicString.testList)

    def test_get_length(self):
         self.assertEqual(len(["1","2","3","4","5"]), 5)

if __name__ == '__main__':
    unittest.main()
