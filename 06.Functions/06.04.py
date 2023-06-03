"""Напишите программу, в которой создается функция с одним текстовым аргументом
и произвольным количеством целочисленных аргументов. Результатом является текст,
сформированный из букв первого текстового аргумента. Целочисленные аргументы определяют
индексы букв, которые нужно включить в текст-результат."""


def pull_out_of_line(line: str, *args: int) -> str:
    lst = [line[i] for i in args if i in range(len(line))]
    return ''.join(lst)


if __name__ == '__main__':
    print(pull_out_of_line("0123456", 4, 3, 9))