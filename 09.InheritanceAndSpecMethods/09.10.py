"""Напишите программу, в которой создается итератор, генерирующий числа Фибоначчи
(первые два числа равны единице, а каждое следующее есть сумма двух предыдущих).
Количество генерируемых чисел передается в качестве аргумента конструктору
при создании итератора."""


class MyClass:
    def __init__(self, amount: int):
        self.amount = amount

    def __iter__(self):
        a = 1
        yield a
        b = 1
        yield b
        for _ in range(self.amount - 2):
            a, b = b, a + b
            yield b


if __name__ == '__main__':
    obj = MyClass(8)
    print(list(obj))
