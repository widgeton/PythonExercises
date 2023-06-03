"""Напишите программу, в которой создается три дочерних потока. В первом потоке вычисляется
факториал числа (произведение натуральных чисел). Во втором потоке вычисляется двойной факториал
числа (произведение чисел через одно). В третьем потоке вычисляется число из последовательности
Фибоначчи (первые два числа равны единице, а каждое следующее равно сумме двух предыдущих)."""
from threading import Thread


def factorial(num: int):
    global f
    f = 1
    for i in range(1, num + 1):
        f *= i


def double_factorial(num: int):
    global g
    g = 1
    for i in range(1, num + 1, 2):
        g *= i


def fibonacci(n: int):
    global h
    if n in [1, 2]:
        return 1
    a = 1
    h = 1
    for i in range(3, n + 1):
        a, h = h, a + h


if __name__ == '__main__':
    f = g = h = None
    t1 = Thread(target=factorial, args=(5,))
    t2 = Thread(target=double_factorial, args=(5,))
    t3 = Thread(target=fibonacci, args=(5,))

    t1.start()
    t2.start()
    t3.start()

    if t1.is_alive():
        t1.join()
    if t2.is_alive():
        t2.join()
    if t3.is_alive():
        t3.join()

    print(f, g, h)
