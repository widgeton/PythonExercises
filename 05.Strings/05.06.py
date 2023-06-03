"""Напишите программу для расшифровки текста, зашифрованного в соответствии
с таким алгоритмом: каждая буква заменяется на следующую, а последняя буква
в алфавите заменяется на первую."""


def encoder(txt: str) -> str:
    lst = list(txt)
    for i, char in enumerate(lst):
        if char == "Я":
            lst[i] = "А"
        elif char == 'я':
            lst[i] = "а"
        elif 'а' <= char < 'я' or 'А' <= char < 'Я':
            lst[i] = chr(ord(char) + 1)

    return ''.join(lst)


def decoder(txt: str) -> str:
    lst = list(txt)
    for i, char in enumerate(lst):
        if char == "А":
            lst[i] = "Я"
        elif char == "а":
            lst[i] = "я"
        elif 'а' < char <= 'я' or 'А' < char <= 'Я':
            lst[i] = chr(ord(char) - 1)

    return ''.join(lst)


text = input("Введите текст на русском: ")
text = encoder(text)
print("Закодированный текст:", text)
text = decoder(text)
print("Раскодированный текст:", text)
