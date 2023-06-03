"""Напишите программу, в которой пользователь вводит две рациональные дроби,
а программа вычисляет сумму, произведение, разность и частное этих дробей, среди
полученных значений находит наибольшее и наименьшее и отображает результат вычислений."""
from fractions import Fraction

numerator1 = input("Введите числитель первой дроби: ")
denominator1 = input("Введите знаменатель первой дроби: ")

numerator2 = input("Введите числитель второй дроби: ")
denominator2 = input("Введите знаменатель второй дроби: ")

if not numerator1.isdigit() or not denominator1.isdigit() or \
        not numerator2.isdigit() or not denominator2.isdigit():
    print("Неверный ввод!")
    exit()

num1 = Fraction(int(numerator1), int(denominator1))
num2 = Fraction(int(numerator2), int(denominator2))

lst = (num1 + num2, num1 * num2, num1 - num2, num1 / num2)
print(min(lst), max(lst))
