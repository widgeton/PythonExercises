"""Напишите программу, в которой пользователю предлагается ввести текст,
а затем в этом тексте, без применения специальных методов (а именно,
не используя метод swapcase()), все большие буквы меняются на маленькие,
а маленькие — на большие."""

txt = input("Введите текст на русском: ")

dif = ord('а') - ord('А')
new_txt = []
for char in txt:
    char = ord(char)
    if ord('я') >= char >= ord('а'):
        new_txt.append(chr(char - dif))
    elif ord('Я') >= char >= ord('А'):
        new_txt.append(chr(char + dif))
    else:
        new_txt.append(chr(char))

print(''.join(new_txt))
