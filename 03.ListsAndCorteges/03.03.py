"""Напишите программу с функцией, которая создает вложенный список.
Размеры списка указываются аргументами функции. Список заполняется
случайными буквами."""
from random import choice


def get_list(rows, columns):
    letters = tuple(i for i in range(ord('a'), ord('z') + 1))
    letters += tuple(i for i in range(ord('A'), ord('Z') + 1))

    lst = [['' for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            lst[i][j] = chr(choice(letters))

    return lst


print(get_list(3, 4))
