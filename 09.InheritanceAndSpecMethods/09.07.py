"""Напишите программу с классом, объекты которого можно индексировать. В частности,
у объекта должно быть два поля-списка с числами. При индексировании объекта возвращается
сумма элементов из списков с соответствующим индексом. Если в каком-то списке нет такого
элемента, он заменяется нулевым значением."""


class MyClass:
    def __init__(self, lst1: list, lst2: list):
        self.lst1 = lst1
        self.lst2 = lst2

    def __getitem__(self, item):
        if len(self.lst1) > len(self.lst2):
            big_lst = self.lst1
            small_lst = self.lst2
        else:
            big_lst = self.lst2
            small_lst = self.lst1

        if item >= len(big_lst):
            return 0

        if item < len(small_lst):
            return big_lst[item] + small_lst[item]

        return big_lst[item]


if __name__ == '__main__':
    obj = MyClass([1, 2, 3], [4, 5, 6, 7])
    print(obj[8])
    print(obj[2])
    print(obj[3])
