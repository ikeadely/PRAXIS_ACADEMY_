## Python program to illustrate
## pickle.dump()
import pickle
import io

class SimpleObject(object):

	def __init__(self, name):
		self.name = name
		l = list(name)
		l.reverse()
		self.name_backwards = ''.join(l)
		return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

## Simulate a file with StringIO
out_s = io.StringIO()

## Write to the stream
for o in data:
	print ('WRITING: %s (%s)' % (o.name, o.name_backwards))
# 	## pickle.dump(o, out_s)
	out_s.flush()


## Python program to illustrate
## Picle.dumps()
import pickle

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
data_string = pickle.dumps(data)
print ('PICKLE:', data_string )

# Python program to illustrate
# pickle.dump()
import pickle
import io

class SimpleObject(object):

	def __init__(self, name):
		self.name = name
		l = list(name)
		l.reverse()
		self.name_backwards = ''.join(l)
		return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

# Simulate a file with StringIO
out_s = io.StringIO()

## Write to the stream
for o in data:
	print ('WRITING: %s (%s)' % (o.name, o.name_backwards))
	## pickle.dump(o, out_s)
	out_s.flush()

## python program to illustrate
## pickle.loads()

import pickle 
import pprint

data1 = [ {'a':'A', 'b':2, 'c':3.0 }]
print ('before:',)
data1_string = pickle.dumps(data1)
data2 = pickle.loads(data1_string)
print ('after:',)
pprint.pprint(data2)
print('same?:', (data1 is data2))
print('equal?:', (data1 == data2))

#^^
# import pickle
# class textreader:
#     """print and number lines in a tect file."""
#     def __init__(self, filename):
#         self.filename = filename 
#         self.file = open(filename)
#         self.lineno = 0
#     def readline(self):
#         self.lineno + 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#         return "%i: %s" % (self.lineno, line)
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#     def __setstate__(self, state):
#         file = open(self.filename)
#         for _ in range(self.lineno):
#             file.readline()
#         self.file = file
# reader = TextReader("GeeksForgeeks.txt")
# print(reader.readline())
# print(reader.readline())
# new_reader = pickle.loads(pickle.dump(reader))
# print(new_reader.readline())

# BELUM
#^^