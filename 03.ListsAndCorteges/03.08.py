"""Напишите программу, в которой создается числовой список. Список
заполняется случайными числами. Затем элементы с четными индексами
сортируются в порядке возрастания, а элементы с нечетными индексами
сортируются в порядке убывания."""
from random import randint

lst = [randint(0, 100) for _ in range(16)]
print(lst)

for i in range(len(lst)):
    for j in range(len(lst) - i - 2):
        if j % 2 == 0 and lst[j] > lst[j + 2]:
            lst[j], lst[j + 2] = lst[j + 2], lst[j]
        if j % 2 != 0 and lst[j] < lst[j + 2]:
            lst[j], lst[j + 2] = lst[j + 2], lst[j]

print(lst)
