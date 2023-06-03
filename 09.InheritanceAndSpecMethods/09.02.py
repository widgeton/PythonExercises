"""Напишите программу, в которой есть класс с переопределенными методами для приведения к разным типам.
В частности, у объекта должны быть поля с целочисленным значением, текстом и действительным числовым значением.
При приведении объекта к целочисленному, текстовому или действительному числовому типу возвращается значение
соответствующего поля."""


class MyClass:
    def __init__(self, a: int, b: float, c: str):
        self.a = a
        self.b = b
        self.c = c

    def __int__(self):
        return self.a

    def __float__(self):
        return self.b

    def __str__(self):
        return self.c


if __name__ == '__main__':
    obj = MyClass(6, 7.8, "MyClass object")
    print(int(obj))
    print(float(obj))
    print(obj)
