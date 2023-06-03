"""Напишите программу, в которой на основе введенного пользователем текста
создается новая текстовая строка. В этой строке по сравнению с исходной символы
меняются местами «через один»: первый символ меняется местами с третьим, четвертый
символ меняется местами с шестым, седьмой меняется местами с девятым и так далее."""

txt = input("Введите текст: ")

lst = list(txt)
for i in range(0, len(lst) - 2, 3):
    lst[i], lst[i + 2] = lst[i + 2], lst[i]

print(''.join(lst))