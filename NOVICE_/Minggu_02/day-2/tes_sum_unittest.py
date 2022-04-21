import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

# setelah itu ketik pip instal nose2 untuk menginstall
pip install nose2
Collecting nose2
  Downloading nose2-0.11.0-py2.py3-none-any.whl (144 kB)
     |████████████████████████████████| 144 kB 172 kB/s 
Collecting coverage>=4.4.1
  Downloading coverage-6.3.2-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (212 kB)
     |████████████████████████████████| 212 kB 1.3 MB/s 
Requirement already satisfied: six>=1.7 in /usr/lib/python3/dist-packages (from nose2) (1.14.0)
Installing collected packages: coverage, nose2
  WARNING: The scripts coverage, coverage-3.8 and coverage3 are installed in '/home/ike/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts nose2 and nose2-3.8 are installed in '/home/ike/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed coverage-6.3.2 nose2-0.11.0

# lalu ketik python3 -m nose, keluar hasil
A lebih besar dari B

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK