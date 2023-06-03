"""Напишите программу, в которой описывается функция с произвольным количеством аргументов.
В качестве результата функция возвращает сумму значений целочисленных аргументов. При вычислении
результата использовать обработку исключений."""


def sum_elem(*args):
    s = 0
    for i in args:
        try:
            if not isinstance(i, int):
                raise ValueError
            s += i
        except ValueError:
            continue
    return s


if __name__ == '__main__':
    print(sum_elem(1, 2, 3.4, 5, '6', 7, '8', 9.8))
