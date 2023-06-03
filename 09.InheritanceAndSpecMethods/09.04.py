"""Напишите программу, в которой для объектов предусмотрены операции сложения с числом,
вычитания числа и вычитания из числа, а также умножения на число и деления на число.
У объекта должно быть поле с числовым значением, и при выполнении указанных операций
они должны выполняться с полем объекта."""
from typing import Union


class MyClass:
    def __init__(self, num):
        self.num = num

    def __add__(self, other: Union[int, float]):
        self.num += other

    def __sub__(self, other: Union[int, float]):
        self.num -= other

    def __rsub__(self, other: Union[int, float]):
        self.num = other - self.num

    def __mul__(self, other: Union[int, float]):
        self.num *= other

    def __truediv__(self, other: Union[int, float]):
        self.num /= other

    def __floordiv__(self, other: Union[int, float]):
        self.num //= other

    def __str__(self):
        return str(self.num)


if __name__ == '__main__':
    obj = MyClass(7)
    print(obj)

    obj + 36
    print(obj)

    obj - 7
    print(obj)

    100 - obj
    print(obj)

    obj * 2
    print(obj)

    obj // 3
    print(obj)

    obj / 2
    print(obj)
