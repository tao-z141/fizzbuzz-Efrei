import unittest
from main import fizzbuzz  

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_number(self):
        self.assertEqual(fizzbuzz(7), "7")

    def test_large_fizz(self):
        self.assertEqual(fizzbuzz(99), "Fizz")

    def test_large_buzz(self):
        self.assertEqual(fizzbuzz(100), "Buzz")

    def test_large_fizzbuzz(self):
        self.assertEqual(fizzbuzz(90), "FizzBuzz")

if __name__ == "__main__":
    unittest.main()
