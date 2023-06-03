"""Напишите программу, в которой решается уравнение вида A(A – 1) x = sin(A),
причем при значении A = 0 должно вычисляться решение x = –1."""
from math import sin

print("Решение уравнения A(A – 1) x = sin(A)\n")

try:
    a = int(input("Введите значение А: "))
    res = sin(a) / (a * (a - 1))
    print("x =", res)
except ZeroDivisionError:
    if a == 0:
        print("x = -1")
    else:
        print("Решений нет")
except ValueError:
    print("Неверный ввод")
