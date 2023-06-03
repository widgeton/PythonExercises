"""Напишите программу, в которой есть функция для заполнения вложенного списка.
Список заполняется натуральными числами «змейкой»: сначала заполняется первая строка,
затем последний столбец (сверху вниз), последняя строка (справа налево), первый столбец
(снизу вверх), вторая строка (слева направо), и так далее."""


def fill_list(rows, columns):
    lst = [[0 for i in range(columns)] for _ in range(rows)]

    num = 0
    start_row = 0
    end_row = rows - 1
    start_column = 0
    end_column = columns - 1
    while True:

        for i in range(start_column, end_column + 1):
            lst[start_row][i] = num
            num += 1
        start_row += 1
        if start_row > end_row:
            break

        for i in range(start_row, end_row + 1):
            lst[i][end_column] = num
            num += 1
        end_column -= 1
        if start_column > end_column:
            break

        for i in range(end_column, start_column - 1, -1):
            lst[end_row][i] = num
            num += 1
        end_row -= 1
        if start_row > end_row:
            break

        for i in range(end_row, start_row - 1, -1):
            lst[i][start_column] = num
            num += 1
        start_column += 1
        if start_column > end_column:
            break

    return lst


rows = 5
columns = 6

for j in fill_list(rows, columns):
    for k in j:
        print(f"{k:^4d}", end="")
    print()
