"""Напишите программу, в которой создается итератор, генерирующий нечетные натуральные числа.
Количество генерируемых чисел определяется аргументом конструктора."""


class MyClass:
    def __init__(self, amount: int):
        self.amount = amount

    def __iter__(self):
        for i in range(self.amount):
            yield i * 2 + 1


if __name__ == '__main__':
    obj = MyClass(8)
    print(list(obj))
