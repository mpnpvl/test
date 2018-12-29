#!/usr/bin/python


def square(size):
    size = (size * 4, size ** 2, ((size * size * 2) ** 0.5))
    print(size)
    pass


square(3)


def seasons(mounth):
    if mounth == 1 or mounth == 12 or mounth == 2:
        print('Зима')
    elif mounth == 5 or mounth == 4 or mounth == 3:
        print('Весна')
    elif mounth == 6 or mounth == 7 or mounth == 8:
        print('Лето')
    elif mounth == 9 or mounth == 10 or mounth == 11:
        print('Осень')
    else:
        print("no seasons")
    pass


seasons(3)


def bank(su, year, pr):
    n = 0.0
    while n <= year:
        su += su * pr / 100 * year
        n += 1
    return su


print(bank(100, 0.2, 10))
