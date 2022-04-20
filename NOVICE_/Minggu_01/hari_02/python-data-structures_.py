# DATA STRUCTURES
# 5.1. More on Lists

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print (fruits.count('apple'))
# print (fruits.count('tangerine'))
# print (fruits.index('banana'))
# print (fruits.index('banana', 4) )
# print (fruits.reverse())
# print (fruits)
# print (fruits.append('grape'))
# print (fruits)
# print (fruits.sort())
# print (fruits)
# print (fruits.pop())

# (belum bisa)

# 5.1.1 using list as stacks

# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print (stack)
# print (stack.pop())
# print (stack)
# print (stack.pop())
# print (stack.pop())
# print (stack)

# 5.1.2. using lisr=st as queues

# from collections import deque
# queue = deque (["eric", "john", "michael"])
# queue.append("terry")
# queue.append("graham")
# print (queue.popleft())
# print (queue.popleft())
# print (queue)

# squares = list(map(lambda x: x**2, range(10)))
# square = [x**2 for x in range(10)]
# print ([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x,y))
# print (combs)


# vec = [-4,-2,0,2,4]
# print ([x*2 for x in vec])
# print ([x for x in vec if x >=0])
# print ([abs (x) for x in vec])

# freshfruit = [ 'banana', 'loganberry', 'passion fruit']
# print ([weapon.strip() for weapon in freshfruit])
# print ([(x,x**2) for x in range (6)])

# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print ([num for elem in vec for num in elem])


#5.1.4. nested list comprehensions

# matrix = [
#      [1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#  ]
#  print([[row[i] for row in matrix] for i in range(4)])
#  (belum bisa)


# 5.2. the del statement 
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print (a)
# del a[2:4]
# print (a)
# del a[:]
# print (a)


# print (del a)


# 5.3. tuples and sequences
# t = 12345, 54321, 'hello!'
# print (t[0])
# print (t)

# u = t, (1,2,3,4,5)
# print (u)

#5.4. sets

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print ('orange' in basket)
# print ('crabgrass' in basket)

# a = set('abracadrabra')
# b = set('alacazam')
# print (a)
# print (a-b)
# print (a | b)
# print (a & b)
# print (a ^ b)

#5.5 dictionaries

# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# print (tel)
# print (tel['jack'])

# del tel['sape']
# tel['irv'] = 4127
# print (tel)

# list(tel)
# print (sorted(tel))

# print ('guido' in tel)
# print ('jack' not in tel)

# 5.6 looping techniques

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)

# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

# for i in reversed(range(1, 10, 2)):
#     print (i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)

# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)

# print (filtered_data)


# latihan 5.7 more on conditions

# string1, string2, string3 = '', 'trondheim', 'hammer dance'
# non_null = string1 or string2 or string3
# print (non_null)
