"""Напишите программу с функцией, аргументом которой передается числовой список,
а результатом является еще один список, в который включены только нечетные числа
из списка-аргумента."""


def odd_nums_from_list(lst: list) -> list:
    return [i for i in lst if i % 2 != 0]


if __name__ == '__main__':
    lst = list(range(10))
    print(odd_nums_from_list(lst))
