class employee:
    a = 1
class Programmer(employee):
    b = 2
class Manager(Programmer):
    c = 3
o = employee()
o = Programmer()
o = Manager()
print(o.a)
print(o.a, o.b, o.c)