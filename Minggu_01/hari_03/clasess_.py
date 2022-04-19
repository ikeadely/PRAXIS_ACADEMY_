# 9.   CLASSES
# 9.2. python scopes and namespaces
# 9.2.1. scopes and namespaces examples

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# 9.3.1. class definitions syntax

class coding():
    name : "nama"

ikan = coding()
iwak = coding()

ikan.name = "ikan ndut"
iwak.name = "iwak mati"

print(ikan.name)
print(iwak.name)

# 9.3.2. class objects

class country():
    village : "district"
    def vacation(self, kondisi):
        print(self.village, "jalan-jalan yok",kondisi)
indonesia = country()
japan = country()

indonesia.village = "indonesia negaraku"
japan.village = "japan apaan tuhh"

print(indonesia.village)
print(japan.village)

indonesia.vacation('keliling indonesia')


# ^^

class healing():
    def __init__(self, village, country, beach):
        self.village = village
        self.country = country
        self.beach = beach 
    def id_gender(self):
        print('village:',self.village, '\ncountry:', self.country, '\nbeach:', self.beach)

class visit(healing):
    def id_gender(self):
        print('ndak tau')

healing1 = healing('pati', 'indonesia', 'all')
healing2 = visit('tuban', 'indonesia', 'home')

healing1.id_gender()
healing2.id_gender()

# 9.3.3. instance objects

# data.counter = 1
# while data.counter < 10:
#     data.counter = data.counter * 2
# print(data.counter)
# del datasssssclear.counter

# belum bisa

# 9.3.4 method object





# 9.3.5 variabel kelas

# class dog:
#     kind = 'canine'
#     def __init__(self,name):
#         self.name = name 

# d = dog('fido')
# e = dog('buddy')
# print(d.kind)
# print('e.kind')
# print(d.name)
# print(e.name)


# 9.4. catatan

# class home:
#     backend = 'belakang'
#     frontend = 'depan'
# w1 = home()
# print(w1.backend, w1.frontend)

# w2 = home()
# w2.frontend = 'tengah'
# print(w2.backend, w2.frontend)


# 9.5. warisan/inheritance

# 9.8.iterator

# for dwi in [1,2,3]:
#     print(dwi)
# for ike in [1,2,3]:
#     print(ike)
# for adel in {'four': 4, 'six': 6}:
#     print(adel)
# for lya in "4646":
    # print(lya)
# for mas in open("workfile1.txt"):
#     print(mas, end='') (for mas gakeluar)

# s = 'abc'
# it = iter(s)
# it
# print(next(it))
# print(next(it))
# print(next(it))

# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopInteration
#         self.index = self.index - 1
#         return self.data[self.index]
# rev = Reverse('spam')
# iter(rev)
# for char in rev:
#     print(char)



# 9.9. generator

# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]
# for char in reverse('golf'):
#     print(char)


# 9.10. ekspresi
# sum(i*i for i in range(10))


# adel = [10, 20, 30]
# lya = [7, 5, 3]
# print(sum(x*y for x,y in zip(adel, lya)))

# data = 'adelya'
# print(list(data[i] for i in range(len(data)-1, -1, -1)))