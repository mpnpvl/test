#!/usr/bin/python


a = (1, 2, 3)
print(type(a))
b = [1, 2, 3]
print(type(b))
c = {1, 2, 3}
print(type(c))
d = dict(short='dict', long='dictionary')
print(type(c))
print(a.__sizeof__(), b.__sizeof__(), ' ', ' ', c.__sizeof__(), d.__sizeof__())
print(d.keys())
