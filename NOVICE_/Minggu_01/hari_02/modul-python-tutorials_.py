#   LATIHAN MODUL

# import sys

# print('The command line arguments are:')
# for i in sys.argv:
#     print(i)

# print('\n\nThe PYTHONPATH is', sys.path, '\n')

# (belum)

# if __name__ == '__main__':
#     print('This program is being run by itself')
# else:
#     print('I am being imported from another module')


# latihan 6. moduls

# def fib(n): 
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# def fib2(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result
 
# (di file fibo)

# 6.2 standars modules

# 6.3 the dir () function

# import fibo, sys
# print (dir(fibo))
# print (dir(sys))

# a = [1, 2, 3, 4, 5]
# import fibo
# fib = fibo.fib
# print (dir())

# import builtins
# print (dir(builtins))

# 6.4. packages

# ..