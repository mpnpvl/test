#!/usr/bin/python

__author__ = 'mpn'

import random
from datetime import datetime


# формат rest и epytext для документации стандарты

def create_numset(lk):
    """Создаем множество для заполнения матрицы"""
    num_set = set()
    # print(type(num_set))
    for a in range(1, lk + 1):
        num_set.add(a)
        # num_set.discard(0)
        # print(num_set)
    return num_set


def create_array(x):
    """ Создание и замолнение матрицы указанного пользователем размера"""
    r = 0
    lkv = x * x
    mno = (create_numset(lkv))
    array = []
    for i in range(x):
        array.append([])
        for j in range(x):
            usl = bool(False)
            while usl is not True:
                el = int(random.randint(1, lkv))
                if el in mno:
                    array[i].append(el)
                    mno.discard(el)
                    usl = True
            r += 1
    return array


def print_matrix(matrix):
    """ Вывод форматированной по виду матрицы на печать"""
    for row in matrix:
        for x in row:
            print("{:4d}".format(x), end="")
        print()
    print()


def check_sum(matr, mi, xl):
    """ Проверка матрицы согласно условиям магического квадрата"""
    ret = bool(True)
    for i in range(xl):
        s = 0
        for j in range(xl):
            s += matr[i][j]
        if s == mi and ret is True:
            ret = bool(True)
        else:
            ret = bool(False)
    for i in range(xl):
        s = 0
        for j in range(xl):
            s += matr[j][i]
        if s == mi and ret is True:
            ret = bool(True)
        else:
            ret = bool(False)
        s = s1 = 0
        for d in range(xl):
            s += matr[d][d]
            s1 += matr[d][xl - d - 1]
        if s == mi and s1 == mi and ret is True:
            ret = bool(True)
        else:
            ret = bool(False)
    return ret


if __name__ == "__main__":
    xz = 3
    try:
        print('Введите размер матрицы: '),
        xz = int(input())
    except(ValueError, TypeError, NameError):
        print("Вы ввели неверное значение, программа заполнит матрицу 3х3")
    else:
        print("Все ОК")
    finally:
        pass

    k = xz * xz
    m = int(xz * (xz * xz + 1) / 2)
    usl = bool()
    print('начал работу :', datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"))
    arr = []
    count = 0
    while usl is not True:
        arr = create_array(xz)
        # print(checksum.__doc__)
        usl = check_sum(arr, m, xz)
        # usl = True
        count += 1
    print('закончил работу :', datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"))
    print_matrix(arr)
