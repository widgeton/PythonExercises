"""Напишите программу, в которой создается вложенный список из случайных чисел.
В матрице, которая реализуется данным вложенным списком, удаляется строка и столбец.
Номер строки и номер столбца, которые нужно удалить, вводятся пользователем."""
from random import randint


def check_matrix(matrix: list[list[int]]) -> None:
    for i in range(1, len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise ValueError("Матрица должна иметь одинаковое количество столбцов в каждом ряду!")


def show_matrix(matrix: list[list[int]]) -> None:
    check_matrix(matrix)
    for j in lst:
        for k in j:
            print(f"{k:^4d}", end="")
        print()
    print()


def del_row_and_column_from_matrix(matrix: list[list[int]], row: int, column: int) -> None:
    check_matrix(matrix)
    if not 0 <= row <= len(matrix):
        raise ValueError("Неверно указан удаляемый ряд")
    if not 0 <= column <= len(matrix[0]):
        raise ValueError("Неверно указан удаляемый столбец")

    del matrix[row - 1]
    for i in matrix:
        del i[column - 1]


lst = [[randint(1, 100) for _ in range(5)] for _ in range(5)]

show_matrix(lst)
del_row_and_column_from_matrix(lst, 2, 3)
show_matrix(lst)
