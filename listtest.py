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

    def test_replace_slice(self):
        result = list(TestBasicString.testList) # copy
        result[2:4] = ["da", "coolest"]
        self.assertEqual(result, ["APRIL", "is", "da", "coolest", "month,", "breeding"])

    def test_get_length(self):
         self.assertEqual(len(["1","2","3","4","5"]), 5)

    def test_iterate(self):
        for index, item in enumerate(TestBasicString.testList): # index and item, use the enumerate function
            if index == 0: self.assertEqual(item, "APRIL")
            if index == 3: self.assertEqual(item, "cruellest")

if __name__ == '__main__':
    unittest.main()
