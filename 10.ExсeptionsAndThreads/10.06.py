"""Напишите программу, в которой с использованием потоков, вычисляется сумма квадратов натуральных чисел.
Сумма вычисляется определенное время, по аналогии с примером из листинга 10.15.
Листинг 10.15:

from threading import *
from time import sleep

def my_sum():
    global num

    k=1
    txt=str(num)
    while my_event.is_set():
        num+=k
        txt+=" + "+str(k)
        print("[", k,"] ", txt," = ", num, sep="")
        k+=1
        sleep(0.3)
        
print("Сумма целых чисел")

t=Thread(target=my_sum)
num=0
my_event=Event()
my_event.set()
t.start()
sleep(2)
my_event.clear()
if t.is_alive():
    t.join()
print("Результат:", num)
"""

from threading import Thread, Event
from time import sleep


def sum_of_squares():
    global num
    k = 1
    while my_event.is_set():
        num += k**2
        print(k**2, end=" ")
        k += 1
        sleep(0.3)
    print()


print("Сумма квадратов целых чисел")

num = 0
t = Thread(target=sum_of_squares)
my_event = Event()

my_event.set()
t.start()
sleep(2)
my_event.clear()

if t.is_alive():
    t.join()

print("Результат:", num)
