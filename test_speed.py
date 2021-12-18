import unittest
import os
import time
from create_file import create_file_with_numbers
from tz import *


class TestSpeed(unittest.TestCase):
    def setUp(self) -> None:
        self.required_number_of_numbers = [10, 100, 1000, 10000, 100000]
        self.number_of_files = len(self.required_number_of_numbers)
        for i in range(self.number_of_files):
            create_file_with_numbers('test_numbers' + str(i + 1),
                                     self.required_number_of_numbers[i])

    def test_speed(self):
        for i in range(self.number_of_files):
            with self.subTest(i=i):
                start_time = time.time()
                main_func('test_numbers' + str(i + 1))
                run_time = time.time() - start_time
                self.assertLess(run_time, 1)

    def tearDown(self) -> None:
        for i in range(self.number_of_files):
            os.remove('test_numbers' + str(i + 1))


if __name__ == '__main__':
    unittest.main()
