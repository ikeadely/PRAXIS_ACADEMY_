# 10. brief tour of the standard library 
# 10.1 operating system interface

# import os
# print(os.getcwd())
# print(os.chdir('/home/ike/adel')
# print(os.system('mkdir music')) 

# import os
# dir(os)
# help(os)

# import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

# # 10.2 file wildcards

# import glob
# glob.glob('*.py')
# ['primes.py', 'random.py', 'quote.py']

# # 10.3 command line arguments
# import sys
# print(sys.argv)

# import argparse
# parser = argparse.ArgumentParser(
#     prog='top',
#     description='Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)

# 10.5. string pattern matching
# import re
# print(re.findall(r'\bsi[a-z]*', 'simple sigap sapa sunyi'))  #bsi, huruf si tersebut menjelaskan huruf yg awalannya si
# print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
# print('three for tree'. replace('three', 'tree'))

# 10.6 mathematics
# import math
# print(math.cos(math.pi / 4))
# print(math.log(1024, 2))

# import random
# print(random.choice(['apple', 'pear', 'banana']))
# print(random.sample(range(100), 10))
# print(random.random())
# print(random.randrange(6))

# import statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.variance(data))

# # 10.7 internet access

# from urllib.request import urlopen
# with urlopen('https://github.com/praxis-academy/akademik/tree/v2.0/kurikulum/enterprise-python/isi.txt') as response:
#     for line in response:
#         line = line.decode()
#         if line.startswith('datetime'):
#             print(line.rstrip())

# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org

# Beware the Ides of March.
# """)
# server.quit()

# 10.8 dates and times

# from datetime import date
# now = date.today()
# print(now)
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# birthday = date(1999,10,31)
# age = now - birthday
# print(age.days)

# 10.9 data compression 
# import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))
# t = zlib.compress(s)
# print(len(t))
# print(zlib.decompress(t))
# print(zlib.crc32(s))

# 10.10 performance measurements

# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# 10.11 quality control
# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)
# import doctest
# doctest.testmod() 

# import unittest
# class TestStatisticalFunctions(unittest.TestCase):
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeError):
#             average(20, 30, 70)
# unittest.main()
