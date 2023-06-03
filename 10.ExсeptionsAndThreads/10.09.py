"""Напишите программу, в которой создается и построчно заполняется двумерный список
(список, элементами которого являются списки). Для заполнения каждой строки
(каждого внутреннего списка) используется отдельный дочерний поток."""
from threading import Thread
from pprint import pprint

row = 5
columns = 7
matrix = [[] for _ in range(row)]


def fill_row(lst: list, size: int, start: int):
    for j in range(start, start + size):
        lst.append(j)


lst_with_threads = []
for i in range(row):
    thrd = Thread(target=fill_row, args=(matrix[i], columns, columns * i))
    lst_with_threads.append(thrd)
    thrd.start()

for i in lst_with_threads:
    if i.is_alive():
        i.join()

pprint(matrix)
