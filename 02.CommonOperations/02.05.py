"""Напишите следующую программу. Пользователь вводит список целочисленных
значений, а также верхнюю границу для вычисления суммы. Программа вычисляет
сумму натуральных чисел, но за исключением тех, которые входят в список.
Например, если пользователь ввел список [2,5,6] и 10 в качестве верхней
границы суммы, то программа должна вычислить сумму чисел от 1 до 10,
но без учета чисел 2, 5 и 6."""

try:
    nums = eval(input("Введите список исключаемых натуральных чисел в формате [2,5,6]: "))
    bound = int(input("Введите верхнюю границу суммы: "))
except:
    print("Неверный ввод!")
    exit()

if not isinstance(nums, list):
    print("Неверный ввод!")
    exit()

for i in nums:
    if not isinstance(i, int):
        print("Неверный ввод!")
        exit()

s = sum(nums)
n = bound * (bound + 1) // 2

print(f"Сумма равна {n - s}")
