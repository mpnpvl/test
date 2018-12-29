#!/usr/bin/python


def create_numset(lk):
    num_set = set()
    # print(type(num_set))
    for i in range(1, lk+1):
        num_set.add(i)
    # num_set.discard(0)
    print(num_set)
    return num_set


a = (1, 2, 3)
print(type(a))
b = [1, 2, 3]
print(type(b))
c = {1, 2, 3}
print(type(c))
d = dict(short='dict1111', long='dictionary', verylong='cwuiehcede')
print(type(d))
print(a.__sizeof__(), ' \n', b.__sizeof__(), ' \n', c.__sizeof__(), ' \n', d.__sizeof__())

print(range(5))

create_numset(5)
