"""Напишите программу, в которой пользователь должен ввести текущий
год и год своего рождения. Программа вычисляет возраст пользователя
и выводит соответствующее сообщение."""

current_year = input("Введите текущий год: ")
year_of_birth = input("Введите год вашего рождения: ")

if current_year.isdigit() and year_of_birth.isdigit():
    current_year = int(current_year)
    year_of_birth = int(year_of_birth)
else:
    print("Неверный ввод!")
    exit()

if current_year > year_of_birth:
    print(f"Вам {current_year - year_of_birth} лет.")
else:
    print("Вы из будущего? Сильно сомневаюсь!")
    exit()
