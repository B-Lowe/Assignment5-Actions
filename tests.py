import unittest
import task
import math
import random
import time


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_circle_area(self):
        # Test random integers
        random.seed(1)
        for i in range(0, 5):
            random_int = random.randint(0, 100)
            self.assertEqual(task.circle_area(random_int), random_int * (math.pi ** 2))

    def test_first_and_last(self):
        # Test list of integers
        # Define random list size
        random.seed(time.time())
        list_size = random.randint(0, 100)
        # Define a list of ints
        list_int = []
        # Add random ints to list
        for i in range(list_size):
            list_int.append(random.randint(0, 100))
        # Assert that the function returns first and last elements of list
        expected = "first: " + list_int[0] + ", last: " + list_int[list_size - 1]
        self.assertEqual(task.first_and_last(list_int), expected)


if __name__ == "__main__":
    unittest.main()
