"""Напишите программу, в которой пользователь вводит целое число, а программа
отображает сумму значений всех битов в бинарном представлении этого числа."""

num = input("Введите целое число: ")

if not num.isdigit():
    print("Неверный ввод!")
    exit()

lst = [int(i) for i in f'{int(num):b}']
print('Сумма битов:', sum(lst))
