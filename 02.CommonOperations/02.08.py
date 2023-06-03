"""Напишите программу, в которой пользователь вводит целое число
от 1 до 7 включительно, а программа выводит название дня недели,
соответствующее этому числу (Понедельник для 1, Вторник для 2,
и так далее)."""

try:
    num = int(input("Введите число от 1 до 7: "))
    if num not in range(1, 8):
        raise Exception
except:
    print("Неверный ввод!")
    exit()

day = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг",
       5: "Пятница", 6: "Суббота", 7: "Воскресенье"}.get(num)

print(f"Это {day}")