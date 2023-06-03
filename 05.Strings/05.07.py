"""Напишите программу для шифрования и дешифрования текста. Текст шифруется так: каждая
буква заменяется на ту, что размещена от нее в алфавите на две позиции влево. Вторая буква
в алфавите заменяется на последнюю. Первая буква в алфавите заменяется на предпоследнюю."""


def encoder(line: str) -> str:
    lst = list(line)
    for i, char in enumerate(line):
        if char == 'а':
            lst[i] = 'ю'
        elif char == 'А':
            lst[i] = 'Ю'
        elif char == 'б':
            lst[i] = 'я'
        elif char == 'Б':
            lst[i] = 'Я'
        elif 'в' <= char <= 'я' or 'В' <= char <= 'Я':
            lst[i] = chr(ord(char) - 2)
    return ''.join(lst)


def decoder(line: str) -> str:
    lst = list(line)
    for i, char in enumerate(line):
        if char == 'ю':
            lst[i] = 'а'
        elif char == 'Ю':
            lst[i] = 'А'
        elif char == 'я':
            lst[i] = 'б'
        elif char == 'Я':
            lst[i] = 'Б'
        elif 'а' <= char <= 'э' or 'А' <= char <= 'Э':
            lst[i] = chr(ord(char) + 2)
    return ''.join(lst)


txt = input("Введите текст на русском: ")
txt = encoder(txt)
print(txt)
txt = decoder(txt)
print(txt)
