"""Напишите программу, в которой генерируется 15 случайных уникальных целых
чисел: 5 чисел попадают в диапазон значений от 1 до 10 и 10 чисел попадают
в диапазон от 10 до 30."""
from random import randint

my_set = set()
while len(my_set) != 5:
    my_set.add(randint(1, 10))

while len(my_set) != 15:
    my_set.add(randint(10, 30))

print(my_set)
