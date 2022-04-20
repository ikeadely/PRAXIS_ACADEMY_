# what does python support

def add(a,b):
    return a+b
plus = add
plus(3,5)
# belum bisa

# lambda

(lambda a, b: a + b)(3, 4)  # returns 7
addition = lambda a, b: a + b
addition(3, 4)
authors = ['Octavia Butler', 'Isaac Asimov', 'Neal Stephenson', 'Margaret Atwood', 'Usula K Le Guin', 'Ray Bradbury']
sorted(authors, key=len)
sorted(authors, key=lambda name: name.split()[-1])
# belum bisa


# functools
val = [1, 2, 3, 4, 5, 6]
list(map(lambda x: x * 2, val))
reduce(lambda: x, y * x * y, val, 1)

def power(base, exp):
     return base ** exp
cube = partial(power, exp=3)
cube(5)

# decorators

