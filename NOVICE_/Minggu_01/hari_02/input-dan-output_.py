#latihan 7 input and output

# 7.1 fancies output formatting

year = 2016
event = 'referendum'
print (f'resuly of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES voted {:2.2%}'.format(yes_votes, percentage))

s = 'Hello, world.'
print (str(s))

print (repr(s))

print (str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

repr((x, y, ('spam', 'eggs')))

# 7.1.1. formatted string literals

import math
print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'sjoerd': 4127, 'jack': 4098, 'dcab':7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels'
print(f'my hovercraft is full of {animals}.')
print(f'my hovercraft is full of {animals!r}.')

# 7.1.2 the string format () method

# print ('we are the {} who says "{}"!'. format('kninghts', 'ni'))

# print('{0} and {1}'. format('spam', 'eegs'))
# print('{1} and {0}'. format('spam', 'eegs'))

# print ('this {food} is {adjective}.'. format(
#     food='spam', adjective='absolutely horrible'))

# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
# (belum bisa)
# table = {'sjoerd': 4127, 'jack': 4098, 'dcab': 86276778}
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# (belum bisa)

for x in range (1, 11):
    print('{0:2d} {1:3d} {2:4d}'. format (x, x*x, x*x*x))

# 7.1.3. manual string formatting

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

print ('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

# 7.1.4. old string formatting
import math
print('The value of pi is approximately %5.3f.' % math.pi)

# 7.2. reading and writing files

f = open('workfile.txt', 'r')

f = open('demo.txt', 'r')
with open('demo.txt') as f:
    read_data = f.read()
    print(read_data)


value = ('the answer', 42)
s = str(value)
print(len(s))

f = open('demo.txt', 'rb+')
print(f.write(b'0123456789abcdef'))
print(f.seek(5))
print(f.read(1))
print(f.seek(-3, 2))
print(f.read(1))

import json
x = [1, 'simple', 'list']
print (json.dumps(x))
