from my_sum import sum
import unittest

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

# Executing your first test
if __name__ == '__main__':
    unittest.main()


# # python3 -m unittest test

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK

# # python3 -m unittest -v test

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK

# # python3 -m unittest discover

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK

# # python3 -m unittest discover -s test
# .....................s.....................
# ----------------------------------------------------------------------
# Ran 43 tests in 7.655s

# OK (skipped=1)

# python3 -m unittest discover -s test -t src
# Traceback (most recent call last):
#   File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
#     return _run_code(code, main_globals, None,
#   File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
#     exec(code, run_globals)
#   File "/usr/lib/python3.8/unittest/__main__.py", line 18, in <module>
#     main(module=None)
#   File "/usr/lib/python3.8/unittest/main.py", line 100, in __init__
#     self.parseArgs(argv)
#   File "/usr/lib/python3.8/unittest/main.py", line 124, in parseArgs
#     self._do_discovery(argv[2:])
#   File "/usr/lib/python3.8/unittest/main.py", line 244, in _do_discovery
#     self.createTests(from_discovery=True, Loader=Loader)
#   File "/usr/lib/python3.8/unittest/main.py", line 154, in createTests
#     self.test = loader.discover(self.start, self.pattern, self.top)
#   File "/usr/lib/python3.8/unittest/loader.py", line 349, in discover
#     tests = list(self._find_tests(start_dir, pattern))
#   File "/usr/lib/python3.8/unittest/loader.py", line 387, in _find_tests
#     name = self._get_name_from_path(start_dir)
#   File "/usr/lib/python3.8/unittest/loader.py", line 371, in _get_name_from_path
#     assert not _relpath.startswith('..'), "Path must be within the project"
# AssertionError: Path must be within the project

# understanding test output

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

def test_list_fraction(self):  """  Test that it can sum a list of fractions  """  data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]  result = sum(data)  self.assertEqual(result, 1) 
if __name__ == '__main__':
    unittest.main()

# python -m unittest test

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
