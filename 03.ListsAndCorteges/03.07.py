"""Напишите программу с функцией, которая для списка, переданного аргументом,
возвращает список из двух элементов: значение наибольшего элемента в списке и
индекс этого элемента в списке (если таких элементов несколько, то индекс
первого из таких элементов)."""
from random import randint


def max_value_and_index(lst: list) -> list:
    max_value = max(lst)
    index_max = lst.index(max_value)
    return [max_value, index_max]


lst = [randint(0, 100) for _ in range(16)]
print(lst)
print(max_value_and_index(lst))
