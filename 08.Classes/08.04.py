"""Напишите программу, в которой описана функция, предназначенная для создания объектов. Функции при вызове
передается список и текстовый аргумент. Текстовый аргумент определяет название класса, на основе которого
создается объект. Текстовые элементы из списка определяют названия полей объекта (нетекстовые аргументы
игнорируются). Значениями полей объекта являются натуральные числа."""
from random import randint


def get_object(lst, class_name):
    class Default:
        def __init__(self):
            for i in lst:
                if isinstance(i, str):
                    self.__dict__[i] = randint(1, 100)

    Default.__name__ = class_name
    return Default()


obj = get_object(['value1', 'value2', 6, 'value3'], 'Values')
print(obj.__dict__, obj.__class__.__name__)

