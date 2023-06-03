"""Напишите программу, в которой для объектов класса предусмотрены операции сравнения.
У каждого объекта есть поле-список с числовыми значениями. Операции сравнения выполняются так:
объекты на предмет равенства проверяются по первому элементу в списках, на предмет «не равно» —
по второму элементу в списках, «меньше» — по третьему элементу в списках, и так далее.
Если соответствующего элемента в списке нет, используется нулевое значение."""


class MyClass:
    def __init__(self, lst: list):
        self.lst = lst

    def __eq__(self, other):
        if len(self.lst) > 0:
            return self.lst[0] == other
        return other == 0

    def __ne__(self, other):
        if len(self.lst) > 1:
            return self.lst[1] != other
        return other != 0

    def __lt__(self, other):
        if len(self.lst) > 2:
            return self.lst[2] < other
        return other > 0

    def __gt__(self, other):
        if len(self.lst) > 3:
            return self.lst[3] > other
        return other < 0

    def __le__(self, other):
        if len(self.lst) > 4:
            return self.lst[4] <= other
        return other >= 0

    def __ge__(self, other):
        if len(self.lst) > 5:
            return self.lst[5] >= other
        return other <= 0


if __name__ == '__main__':
    obj = MyClass([0, 1, 2, 3, 4, 5, 6])
    print(obj == 3)
    print(obj != 3)
    print(obj < 3)
    print(obj > 3)
    print(obj <= 3)
    print(obj >= 3)
