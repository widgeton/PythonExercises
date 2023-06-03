"""Напишите программу, в которой пользователь вводит целое число,
а программа формирует кортеж, который состоит из цифр, входящих в это число.
Предложите способы создания кортежа, при котором цифры, формирующие число,
включаются в кортеж в прямом и обратном порядке."""

num = input("Введите целое число: ")

if not num.isdigit():
    print("Неверный ввод!")
    exit()

n = int(num)
revers_tpl = tuple()
while n > 0:
    revers_tpl += (n % 10,)
    n //= 10

n = int(num)
straight_tpl = tuple()
while n > 0:
    straight_tpl = (n % 10,) + straight_tpl
    n //= 10

print(straight_tpl)
print(revers_tpl)
