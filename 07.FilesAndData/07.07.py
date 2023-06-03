"""Напишите программу, в которой пользователь вводит две даты, а программа
определяет количество полных дней между этими датами."""
from datetime import date

date1 = input("Введите первую дату в формате 2020-11-5 (год-месяц-день): ")
date2 = input("Введите вторую дату в формате 2020-11-5 (год-месяц-день): ")

date1 = [int(i) for i in date1.split('-')]
date2 = [int(i) for i in date2.split('-')]

try:
    print(abs((date(*date1) - date(*date2)).days))
except ValueError as vr:
    print("Wrong input,", vr)
