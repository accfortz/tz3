import unittest
import os
from create_file import *
from tz import *


class TestIncorrectInput(unittest.TestCase):
    def setUp(self) -> None:
        create_file_with_numbers('blank_file.txt', 0)
        create_wrong_file('wrong_file')

    def test_blank_file(self):
        self.assertEqual(main_func('blank_file.txt'), None)

    def test_wrong_file(self):
        with self.assertRaises(ValueError):
            main_func('wrong_file')

    def tearDown(self) -> None:
        os.remove('blank_file.txt')
        os.remove('wrong_file')


if __name__ == '__main__':
    unittest.main()
