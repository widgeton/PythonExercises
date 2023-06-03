"""Напишите программу, в которой пользователь вводит целое число, а программа переводит
его в восьмеричную систему, меняет порядок следования цифр в представлении числа и
результат отображает в области вывода."""

num = input("Введите число: ")

if not num.isdigit():
    print("Ввод не верный!")
    exit()

num = int(num)
rev_oct_num = 0
digit = 1
while num > 0:
    num, s = divmod(num, 8)
    rev_oct_num = rev_oct_num * 10 + s
    digit *= 10

print(rev_oct_num)
