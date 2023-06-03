"""Напишите программу, в которой пользователь вводит момент времени, а программа определяет
интервал между текущим моментом и моментом времени, который указал пользователь."""
from datetime import date

dt = input("Введите дату в формате 2020-11-5 (год-месяц-день): ")
dt = [int(i) for i in dt.split('-')]

try:
    print(abs((date.today() - date(*dt)).days), "дней разницы")
except ValueError as vr:
    print("Wrong input,", vr)
