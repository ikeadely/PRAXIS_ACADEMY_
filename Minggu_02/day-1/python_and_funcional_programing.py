# FUNGSIONAL AS FIRST CLASS ONJECTS IN PYTHON

print(list(map(int, ["1", "2", "3"])))

# ^^
# def hello_world(h):
#     def world(w):
#         print(h, w)
#     return world

# h = hello_world
# x = h("hello")
# x
# (function world at 0x7fec47afc668)
# x("world")
# print (x("world")

# function_list = [h, x]
# function_list
# print([<function hello_world at 0x7fec47afc5f0>, <function qorld at 0x7fec47afc5f0>])

# belum bisa
# ^^

# PYTHON FUNGSIONAL PURITY

# def naive_sum(list):
#     s = 0
#     for l in list:
#         s += l
#     return s
# sum(list)
# belum bisa

# REDUCING THE USAGE OF LOOPS IN PYTHON

# for x in l:
#     func(x)
# map(func, l)
# def func1():
#     pass
# def func2():
#     pass
# def func3():
#     pass
# executing = lambda f: f()
# map(executing, [func1, func2, func3])
# belum bisa