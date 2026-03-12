import unittest
from Zaj_1.main import Add

class TestAdd(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Add(""), 0)

    def test_one_number(self):
        self.assertEqual(Add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(Add("1, 2"), 3)
        self.assertEqual(Add("1\n2"), 3)

    def test_many_numbers(self):
        self.assertEqual(Add("1, 2, 3"), 6)
        self.assertEqual(Add("1\n2\n3"), 6)

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            Add("1, dwa")

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            Add("1,-2")


unittest.main(argv=['first-arg-is-ignored'], exit=False)
