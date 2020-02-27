import unittest
import task
import math
import random


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


if __name__ == "__main__":
    unittest.main()
