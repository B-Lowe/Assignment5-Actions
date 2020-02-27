import unittest
import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_circle_area(self):
        self.assertEqual(task.circle_area(1), (math.pi ** 2))
        self.assertEqual(task.circle_area(2), 2 * (math.pi ** 2))
        self.assertEqual(task.circle_area(3), 3 * (math.pi ** 2))


if __name__ == "__main__":
    unittest.main()
