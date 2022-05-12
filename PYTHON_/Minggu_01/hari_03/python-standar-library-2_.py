# 11. brief tour of the standard library part 2
# 11.1 output formatting
import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
print(pprint.pprint(t, width=30))

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

import locale
print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))
conv = locale.localeconv()
x = 1234567.8
print(locale.format("%d", x, grouping=True))

print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True))

# 11.2 templating

from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
## print(t.substitu(d))
print(t.safe_substitute(d))

# ^^
# import time, os.path
# photofiles = ['img-12.jpeg','img-11.jpg']
# class BatchRename(Template):
#     delimiter = '%'
# print(fmt = input('Enter rename style (%d-date %n-seqnum): '))

# t = BatchRename(fmt)
# date = time.strtime('%d%b%y')
# for i, filename in enumerate(photofiles):
#     base, ext = os.path.splitext(filename)
#     newname = t.substitute(d=date, n=i, f=ext)
#     print('{0} --> {1}'.format(filename, newname))
# ^^


# 11.3 working with binary data record layouts

# import struct
# with open('myfile.zip', 'rb') as f:
#     data = f.read()
# start = 0
# for i in range(3):
#     start += 14
#     fields = struct.unpack('<IIIHH', data[start:start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
#     start += 16
#     filename = data[start:start+filenamesize]
#     start += filenamesize
#     extra = data[start:start+extra_size]
#     print(filename, hex(crc32), comp_size, uncomp_size)
#     start += extra_size + comp_size 

#(belum ketemu)

# 11.4. multi-threading

import threading, zipfile
class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)
background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')
background.join()
print('Main program waited until background was done.')

# 11.5 logging

import logging 
print(logging.debug('debuging information'))
print(logging.info('informasional message'))
print(logging.warning('warning:config file %s not found', 'server.conf'))
print(logging.error('error occured'))
print(logging.critical('critical error -- shutting down'))

# 11.6 weak references

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a 
print(d['primary']) 
del a 
print(gc.collect())

# 11.7 tools for working with lists

from array import array
a = array('H', [4000, 10, 700,22222])
print(sum(a))
print(a[1:3])

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

# ^^
# unsearched = deque([starting_node])
# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     for m in gen_moves(node):
#         return m 
#     unsearched.append(m)
# (belum bisa)
# ^^

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

from heapq import heapify, heappop, heappush
data = [1,3,5,7,9,2,4,6,8,0]
heapify(data)
heappush(data, -5)
print([heappop(data) for i in range(3)])

# 11.8 decimal floating point aritchmetic

from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'),2))
print(round(.70 * 1.05, 2))

print(Decimal('1.00') % Decimal('.10'))
print(1.00 % 0.10)

print(sum([Decimal('0.1')]*10)== Decimal('1.0'))
print(sum([0.1]*10) == 1.0)

getcontext().prec = 36
print(Decimal(1) / Decimal(7))