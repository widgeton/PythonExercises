"""Напишите программу для решения уравнения Ax = B – A – 1. Параметры A и B вводятся пользователем.
Уравнение имеет решение x = (B – 1) / A – 1 если A ≠ 0. При A = 0 и B = 1 решением является любое
число, а при A = 0 и B ≠ 1 решений у уравнения нет. Предложите разные варианты программы,
в том числе и с использованием обработки исключительных ситуаций."""


def try_except_solution():
    print("Решение уравнения Ax = B – A – 1.")
    try:
        a = int(input("Введите целое значение для А: "))
        b = int(input("Введите целое значение для B: "))
        result = (b - 1) / a - 1
        print(f"Уравнение имеет одно решение: x = {result:.3f}")
    except ValueError:
        print("Неверный ввод!")
    except ZeroDivisionError:
        if b == 1:
            print("Решением является любое число")
        else:
            print("Уравнение не имеет решений")


def branching_solution():
    print("Решение уравнения Ax = B – A – 1.")

    a = input("Введите целое значение для А: ")
    b = input("Введите целое значение для B: ")

    if not a.isdigit() or not b.isdigit():
        print("Неверный ввод")
        return

    if a == "0" and b == "1":
        print("Решением является любое число")
    elif a == "0" and b != "1":
        print("Уравнение не имеет решений")
    elif a != "0":
        result = (int(b) - 1) / int(a) - 1
        print(f"Уравнение имеет одно решение: x = {result:.3f}")


# try_except_solution()
branching_solution()
