# Test cases for fizzbuzz function

import sys
import unittest
from io import StringIO

from main import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """
    Test cases for fizzbuzz function
    """

    def setUp(self):
        """
        Redirect stdout to StringIO
        :return:
        """
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        """
        Reset stdout
        :return:
        """
        sys.stdout = self.held

    def test_fizzbuzz_divisible_by_3_and_5(self):
        """
        Test fizzbuzz function with 15
        :return:
        """
        fizzbuzz(15)
        self.assertEqual(sys.stdout.getvalue().strip(), "FizzBuzzBuzz")

    def test_fizzbuzz_divisible_by_3(self):
        """
        Test fizzbuzz function with 9
        :return:
        """
        fizzbuzz(9)
        self.assertEqual(sys.stdout.getvalue().strip(), "Fizz")

    def test_fizzbuzz_divisible_by_5(self):
        """
        Test fizzbuzz function with 10
        :return:
        """
        fizzbuzz(10)
        self.assertEqual(sys.stdout.getvalue().strip(), "Buzz")

    def test_fizzbuzz_contains_3(self):
        """
        Test fizzbuzz function with 13
        :return:
        """
        fizzbuzz(13)
        self.assertEqual(sys.stdout.getvalue().strip(), "13Fizz")

    def test_fizzbuzz_contains_5(self):
        """
        Test fizzbuzz function with 52
        :return:
        """
        fizzbuzz(52)
        self.assertEqual(sys.stdout.getvalue().strip(), "52Buzz")

    def test_fizzbuzz_not_divisible_or_contains_3_or_5(self):
        """
        Test fizzbuzz function with 7
        :return:
        """
        fizzbuzz(7)
        self.assertEqual(sys.stdout.getvalue().strip(), "7")


if __name__ == "__main__":
    unittest.main()
