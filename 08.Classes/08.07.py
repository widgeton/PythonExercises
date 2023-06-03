"""Напишите программу, в которой описана функция. В качестве аргументов функции передаются два объекта
одного и того же класса. У каждого объекта есть поле, представляющее собой список из целых чисел.
В результате функция возвращает объект того же класса. Поле-список этого объекта получается суммированием
соответствующих элементов из полей-списков объектов, переданных аргументами функции. Если в этих объектах
списки разной длины, то недостающие элементы в списке заменяются нулями."""
from random import randint


class MyClass:
    def __init__(self, val: list[int]):
        self.val = val


def sum_lists_objs(obj1: MyClass, obj2: MyClass) -> MyClass:
    lst = []
    for i in range(min(len(obj1.val), len(obj2.val))):
        lst.append(obj1.val[i] + obj2.val[i])
    largest = obj1 if len(obj1.val) > len(obj2.val) else obj2
    lst.extend(largest.val[i + 1:])
    return MyClass(lst)


if __name__ == '__main__':
    obj1 = MyClass([randint(-100, 100) for _ in range(8)])
    obj2 = MyClass([randint(-100, 100) for _ in range(4)])
    obj = sum_lists_objs(obj1, obj2)

    print(obj1.val)
    print(obj2.val)
    print(obj.val)
