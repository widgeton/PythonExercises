"""Напишите программу, в которой создается цепочка наследования из трех классов.
У объекта исходного класса имеется поле, и у каждого следующего класса добавляется
по одному полю. Опишите методы, переопределяемые в производных классах, которые позволяют
присваивать значения полям и отображать значения полей."""


class First:
    def __init__(self, a):
        self.a = a

    def show_fields(self):
        print(f"a = {self.a}")


class Second(First):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def show_fields(self):
        super().show_fields()
        print(f"b = {self.b}")


class Third(Second):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def show_fields(self):
        super().show_fields()
        print(f"c = {self.c}")


if __name__ == '__main__':
    objFirst = First(2)
    objSecond = Second(3, 4)
    objThird = Third(5, 6, 7)

    objFirst.show_fields()
    objSecond.show_fields()
    objThird.show_fields()
    