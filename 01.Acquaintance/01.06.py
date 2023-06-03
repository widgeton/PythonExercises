"""Напишите программу, в которой проверяется, делится ли введенное
пользователем число на 3. Учесть, что если число делится на 3, то остаток
от деления этого числа на 3 равен нулю."""

MULTIPLE = 3
number = input("Введите целое число: ")

if not number.isdigit():
    print("Неверный ввод!")
    exit()

if int(number) % MULTIPLE == 0:
    print(f"Число {number} кратно {MULTIPLE}")
else:
    print(f"Число {number} НЕ кратно {MULTIPLE}")
