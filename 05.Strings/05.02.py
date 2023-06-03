"""Напишите программу, в которой с использованием операторов цикла и форматированных
литералов, символом «звездочка» * в области вывода отображается буква "A"."""

char = "*"
length = 6
gape = " "
for i in range(length):
    if i == length // 2:
        gape = char * i * 2 + char
    print(f"{char:>{length - i}s}", end="")
    print(f"{gape:{i * 2 + 1}s}", end="")
    print(f"{char:<{length - i}s}")
    if i == length // 2:
        gape = " "
