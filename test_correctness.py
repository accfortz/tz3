import unittest
from functools import reduce
from random import randint
from tz import min_of_numbers, max_of_numbers, sum_of_numbers, \
    multiplication_of_numbers


class TestNumbersFunctions(unittest.TestCase):
    def setUp(self):
        self.test_list1 = [randint(0, 100) for _ in range(10)]
        self.test_list2 = [randint(-100, 0) for _ in range(10)]
        self.test_list3 = [randint(-100, 100) for _ in range(10)]

    def test_min_of_numbers(self):
        self.assertEqual(min_of_numbers(self.test_list1), min(self.test_list1))
        self.assertEqual(min_of_numbers(self.test_list2), min(self.test_list2))
        self.assertEqual(min_of_numbers(self.test_list3), min(self.test_list3))

    def test_max_of_numbers(self):
        self.assertEqual(max_of_numbers(self.test_list1), max(self.test_list1))
        self.assertEqual(max_of_numbers(self.test_list2), max(self.test_list2))
        self.assertEqual(max_of_numbers(self.test_list3), max(self.test_list3))

    def test_sum_of_numbers(self):
        self.assertEqual(sum_of_numbers(self.test_list1), sum(self.test_list1))
        self.assertEqual(sum_of_numbers(self.test_list2), sum(self.test_list2))
        self.assertEqual(sum_of_numbers(self.test_list3), sum(self.test_list3))

    def test_multiplication_of_numbers(self):
        self.assertEqual(multiplication_of_numbers(self.test_list1),
                         reduce(lambda x, y: x * y, self.test_list1))
        self.assertEqual(multiplication_of_numbers(self.test_list2),
                         reduce(lambda x, y: x * y, self.test_list2))
        self.assertEqual(multiplication_of_numbers(self.test_list3),
                         reduce(lambda x, y: x * y, self.test_list3))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
