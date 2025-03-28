import unittest
from src.lottery import lottery


class TestLottery(unittest.TestCase):

    def test_one_number_with_target_frequency(self):
        self.assertEqual([1], lottery([1, 1, 3, 2, 2, 2, 2, 4, 5], 2))

    def test_multiple_numbers_with_target_frequency(self):
        self.assertEqual([1, 5], lottery([1, 2, 2, 2, 3, 4, 5, 5, 1], 2))

    def test_number_with_three_occurrences(self):
        self.assertEqual([2], lottery([1, 1, 2, 2, 2, 3, 4, 5], 3))

    def test_no_numbers_with_target_frequency(self):
        self.assertEqual([], lottery([1, 1, 2, 2, 2, 3, 4, 5], 7))

    def test_none_numbers(self):
        self.assertEqual([], lottery(None, 1))

    def test_none_size(self):
        self.assertEqual([], lottery([1, 2, 3], None))

    def test_both_none(self):
        self.assertEqual([], lottery(None, None))

    def test_empty_list(self):
        self.assertEqual([], lottery([], 5))


if __name__ == '__main__':
    unittest.main()