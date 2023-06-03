"""Напишите программу, в которой с использованием двух дочерних потоков заполняется список.
Первый поток присваивает буквенные значения элементам с четными индексами. Второй поток присваивает
числовые значения элементам с нечетными индексами."""

from threading import Thread, Lock
from time import sleep


def set_literals(n):
    global lst
    lit = 'a'
    for _ in range(n):
        lock.acquire()
        try:
            lst.append(lit)
            lit = chr(ord(lit) + 1)
        finally:
            lock.release()
            sleep(0.1)


def set_numbers(n):
    global lst
    num = 1
    for _ in range(n):
        lock.acquire()
        try:
            lst.append(num)
            num += 1
        finally:
            lock.release()
            sleep(0.1)


lock = Lock()
lst = []

t1 = Thread(target=set_literals, args=(5,))
t2 = Thread(target=set_numbers, args=(5,))

t1.start()
t2.start()

if t1.is_alive():
    t1.join()

if t2.is_alive():
    t2.join()

print(lst)
