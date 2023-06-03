"""Напишите программу, в которой создается два списка одинакового размера.
На основе этих списков поочередной вставкой элементов из первого и второго
списка формируется новый список."""
from random import randint

length = 5

lst1 = [randint(0, 100) for _ in range(length)]
lst2 = [randint(0, 100) for _ in range(length)]

print(lst1)
print(lst2)

lst = []
for i in range(length):
    lst.append(lst1[i])
    lst.append(lst2[i])

print(lst)
