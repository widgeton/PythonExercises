"""Напишите программу, в которой описывается функция, предназначенная для создания объекта.
Объект создается на основе уже существующего объекта, который передается функции в качестве аргумента.
В создаваемый объект добавляются только те неслужебные поля из исходного объекта, которые имеют
целочисленное значение."""
from copy import deepcopy


class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


def get_obj(obj: MyClass) -> MyClass:
    new_obj = deepcopy(obj)
    for key, value in obj.__dict__.items():
        if not isinstance(value, int):
            del new_obj.__dict__[key]
    return new_obj


if __name__ == '__main__':
    inst = MyClass(1, 'j', 5)
    print(inst.__dict__)
    inst2 = get_obj(inst)
    print(inst2.__dict__)
