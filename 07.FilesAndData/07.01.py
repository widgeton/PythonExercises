"""Напишите программу, в которой пользователь вводит основание для системы счисления
и число (в десятичной системе), а программа отображает это число в соответствующей
системе счисления."""

scale = input("Введите основание для системы исчисления от 2 до 36: ")
num = input("Введите целое число в десятичной системе исчисления: ")

if not scale.isdigit() or not num.isdigit() or not 2 <= int(scale) <= 36:
    print("Неверный ввод!")
    exit()

alphabet = {10 + i: chr(ord('A') + i) for i in range(26)}

scale = int(scale)
num = int(num)

result = ''
while num > 0:
    num, s = divmod(num, scale)
    if scale > 10 and s >= 10:
        s = alphabet[s]
    else:
        s = str(s)
    result = s + result

print(result)
