"""Напишите программу, в которой на основе текста, введенного пользователем,
создается новый текст, в котором по сравнению с исходным удалено самое длинное
и самое короткое слово. Если таких слов несколько, то удаляется первое из них.
Под словами подразумевать блоки текста, разделенные пробелами."""

txt = input("Введите текст: ")

lst = txt.split()
short = 0
long = 0
for i, word in enumerate(lst):
    if len(lst[short]) > len(word):
        short = i
    if len(lst[long]) < len(word):
        long = i

if short == long:
    del lst[short]
elif short > long:
    del lst[long], lst[short - 1]
elif short < long:
    del lst[short], lst[long - 1]

print(' '.join(lst))
