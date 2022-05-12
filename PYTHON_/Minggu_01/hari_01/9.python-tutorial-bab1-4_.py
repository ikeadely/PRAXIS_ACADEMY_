# jenis python 
# Python 2.7.18 (default, Mar  8 2021, 13:02:45) 
# [GCC 9.3.0] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 

# latihan 2.1.2 interactive mode
the_world_is_flat = True 
if the_world_is_flat:
    print("ciee penganut bumi datar")

# 3.1.1 numbers
a = 2
b = 2
print (a+b)

a = 50
b = 5
c = 6
d = 4
print (a - b*c)
print (a - b*c / d)

a = 17
b = 3
c = 5
d = 2
e = 7
print (a/b)
print (a//b)
print (a%b)
print (c*b+d)
print (c**d)
print (d**e)

width = 20
height = 5 * 9
print (width*height)

a = 4
b = 3.75
c = 1
print (a*b-c)

tax = 12.5 / 100
price = 100.50
print (price*tax)
# print (price + _)
# round(_,2)


# 3.1.2 strings
print ('spam eggs')
print ('doesn\'t')
print ("doesn't")
print ('"yes," they said.')
print ("\yes,\ they said")
print ('"isn\'t," they said.')

'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'
print(s)

print('C:\some\name') 
print(r'C:\some\name')

print(3 * 'un' + 'ium')

print ('py' 'thon')

text = ('Dwike'
        'Adelya.')
print(text)

prefix = "py"
print (prefix + 'thon')

word = "python"
print(word[0])
print(word[5])
print(word[-1])
print(word[:2]+word[2:]



word = "Jthon"
print(word[:2])

s = 'supercalifragilisticexpialidocious'
print (len(s))

squares = [1,4,9,16,25]
print (squares)
print (squares[0])


letters = ['a', 'b', 'c', 'd', 'e']
print (letters)
print (len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print (x)
print (x[0])

# soal nomor 4.1 if statements

x = int(input("please enter an interger : "))
if x < 0 :
    x = 0
    print ('negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('more')


soal nomor 4.2 for statement

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len (w))

# soal nomor 4.3 the range () function


for i in range(5):
    print(i)

for i in range(5,10):
    print(i)

a = ['mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for i in range (10):
    print (sum(range(i)))

for i in range(10, 20):
    print (list(range(i)))

# latihan 4.4 break and continue statements and else Clauses on Loops

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # loop fell trought without finding a factor
            print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("found an ever number", num)
        continue
    print("found an odd number", num)

# latihan 4.5 pass statements
pass hasilnya kosong 


while True:
    pass  # busy-wait for keyboard interrupt (Ctrl+C)

class MyEmptyClass:
    pass

# contoh latihan 4.6 match statements untuk python 3.10.4

def http_error(status):
    match (status):
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


# latihan 4.7 defining functions

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(1500)

fib 
f = fib 
f(100)

fib(0)
print(fib(0))


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
f100

# latihan 4.8 more on defining functions

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries -1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# (GABISA)

i = 5 

def f(arg=i):
    print(arg)
i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a,L=None):
    if L is  None:
        L = []
    L.append(a)
    return L

latihan 4.8 keywoard Arguments
disambung dari def f sampai parrot 1000

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("--This parrot woulsn't", action, end='')
    print("if you put", voltage, "volts through it.")
    print("--Lovely plumage, the", type)
    print("--I'ts", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='VOOOOOM')
parrot(action='VOOOOOM', voltage=1000000)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')

def function(a):
    pass

function(0, a=0)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# latihan 4.8.3.4. function examples

def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)
standard_arg(arg=2)

pos_only_arg(1)
pos_only_arg("coba")
kwd_only_arg(3)
kwd_only_arg(arg=3)


combined_example(1, 2, 3)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
combined_example(pos_only=1, standard=2, kwd_only=3)
(type error gabisa)

# 4.8.6 lambda exspressions

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print (f(0))
print (f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print (pairs)


# 4.8.7 documentatation strings

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

# 4.8.8 function annotations

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
