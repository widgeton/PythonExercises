"""Напишите программу, в которой шифруется и дешифруется введенный пользователем текст.
При шифровании каждая буква заменяется на следующую (а последняя — на первую), но только
эта операция отдельно выполняется для гласных букв и для согласных. Для этого нужно
сформировать список гласных и согласных букв и шифрование и дешифрование выполнять на
основе этих списков."""

vowels = ('А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е')
consonants = ('Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М',
              'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ')


def encoder(line: str) -> str:
    lst = list(line)
    for i, char in enumerate(line):
        if char.lower() == consonants[-1].lower():
            if char.islower():
                lst[i] = consonants[0].lower()
            else:
                lst[i] = consonants[0]
        if char.lower() == vowels[-1].lower():
            if char.islower():
                lst[i] = vowels[0].lower()
            else:
                lst[i] = vowels[0]
        if char.upper() in vowels[:-1]:
            if char.islower():
                lst[i] = vowels[vowels.index(char.upper()) + 1].lower()
            else:
                lst[i] = vowels[vowels.index(char) + 1]
        if char.upper() in consonants[:-1]:
            if char.islower():
                lst[i] = consonants[consonants.index(char.upper()) + 1].lower()
            else:
                lst[i] = consonants[consonants.index(char) + 1]
    return ''.join(lst)


def decoder(line: str) -> str:
    lst = list(line)
    for i, char in enumerate(line):
        if char.lower() == consonants[0].lower():
            if char.islower():
                lst[i] = consonants[-1].lower()
            else:
                lst[i] = consonants[-1]
        if char.lower() == vowels[0].lower():
            if char.islower():
                lst[i] = vowels[-1].lower()
            else:
                lst[i] = vowels[-1]
        if char.upper() in vowels[1:]:
            if char.islower():
                lst[i] = vowels[vowels.index(char.upper()) - 1].lower()
            else:
                lst[i] = vowels[vowels.index(char) - 1]
        if char.upper() in consonants[1:]:
            if char.islower():
                lst[i] = consonants[consonants.index(char.upper()) - 1].lower()
            else:
                lst[i] = consonants[consonants.index(char) - 1]
    return ''.join(lst)


txt = input("Введите строку на русском: ")
txt = encoder(txt)
print(txt)
txt = decoder(txt)
print(txt)
