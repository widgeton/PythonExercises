"""Напишите программу, в которой пользователь вводит целое число, а программа
определяет, сколько в этом числе цифр 0, 1, 2 и так далее, до 9."""

n = input("Введите целое число: ")

if not n.isdigit():
    print("Неверный ввод!")
    exit()

num = int(n)
digits_dict = {}
while num > 0:
    digit = num % 10
    if digit in digits_dict:
        digits_dict[digit] += 1
    else:
        digits_dict[digit] = 1
    num //= 10

print(f"В числе {n} встречается:")
for key, value in digits_dict.items():
    print(f"{value} раз(а) цифра {key}")
