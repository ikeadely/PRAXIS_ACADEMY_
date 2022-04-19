# LATIHAN 6. MODULS

def fib (n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))



# import fibo
# print(fibo.fib(1000))
# print(fibo.fib2(100))
# print(fibo.__name__)

# fib = fibo.fib
# print (fib(500))