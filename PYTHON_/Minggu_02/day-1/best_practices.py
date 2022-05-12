# BELUM BISA

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

def retry(func):
    def retried_function(*args, **kwargs):
        exc = None
        for _ in range(3):
            try:
               return func(*args, **kwargs)
            except Exception as exc:
               print("Exception raised while calling %s with args:%s, kwargs: %s. Retrying" % (func, args, kwargs).
        raise exc
     return retried_function
@retry
def do_something_risky():
retried_function = retry(do_something_risky)
# belum

# pure functions

dictionary = ['fox', 'boss', 'orange', 'toes', 'fairy', 'cup']
def puralize(words):
   for i in range(len(words)):
       word = words[i]
       if word.endswith('s') or word.endswith('x'):
           word += 'es'
       if word.endswith('y'):
           word = word[:-1] + 'ies'
       else:
           word += 's'
       words[i] = word
def test_pluralize():
    result = pluralize(dictionary)
    assert result == ['foxes', 'bosses', 'oranges', 'toeses', 'fairies', 'cups']
# ndak tau

# understanding and avoiding mutability

def add_bar(items=[]):
    items.append('bar')
    return items

l = add_bar()
l.append('foo')
add_bar()
# ???

# limiting use of classes

from collections import namedtuple
VerbTenses = namedtuple('VerbTenses', ['past', 'present', 'future'])
class VerbTenses(object):
    def __init__(self, past, present, future):
        self.past = past,
        self.present = present
        self.future = future

class Bus(object):
     passengers = set()
     def add_passenger(self, person):
        self.passengers.add(person)

bus1 = Bus()
bus2 = Bus()
bus1.add_passenger('abe')
bus2.add_passenger('bertha')
bus1.passengers
bus2.passengers

# BELUM BISA

