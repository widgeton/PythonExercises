"""Напишите программу, в которой описана функция, возвращающая результатом
сумму нечетных чисел. Количество чисел передается аргументом функции."""


def sum_odd_nums(amount: int) -> int:
    return sum(i * 2 + 1 for i in range(amount))


num = input("Введите количество нечетных чисел: ")

if not num.isdigit():
    print("Неверный ввод!")
    exit()

print(sum_odd_nums(int(num)))
