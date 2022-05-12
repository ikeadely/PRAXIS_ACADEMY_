# UNDERSTANDING TEST

from fractions import Fraction

import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

# python3 -m unittest try
# F.
# ======================================================================
# FAIL: test_list_fraction (try.TestSum)
# Test that it can sum a list of fractions
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/ike/praxis-academy/NOVICE_/Minggu_02/day-2/project/try.py", line 23, in test_list_fraction
#     self.assertEqual(result, 1)
# AssertionError: Fraction(9, 10) != 1

# ----------------------------------------------------------------------
# Ran 2 tests in 0.018s

# FAILED (failures=1)