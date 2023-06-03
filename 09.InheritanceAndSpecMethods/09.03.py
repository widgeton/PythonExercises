"""Напишите программу, в которой для объектов класса определена операция сложения.
У каждого объекта есть поле-список, и при сложении объектов получается новый объект
того же класса. Его поле-список получается объединением полей-списков исходных объектов."""


class MyClass:
    def __init__(self, lst: list):
        self.lst = lst

    def __add__(self, other):
        lst = self.lst + other.lst
        return MyClass(lst)


if __name__ == '__main__':
    obj1 = MyClass([1, 2, 3, 4])
    obj2 = MyClass([5, 6, 7, 8])
    obj = obj1 + obj2
    print(obj.lst)
    