"""Напишите программу, в которой используется функция-генератор, создающая
итерируемый объект со степенями двойки. Количество элементов определяется
аргументом функции-генератора."""


def generator(amount):
    num = 1
    while amount:
        num *= 2
        yield num
        amount -= 1


print(list(generator(5)))
