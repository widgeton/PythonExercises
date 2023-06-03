"""Напишите программу, в которой для объектов класса предусмотрен специальный режим доступа к полям.
В частности, у объекта должно быть поле-список, значением которому можно присваивать только список.
Из присваиваемого списка в поле-список копируются только текстовые значения. При считывании значения
этого поля возвращается текстовая строка, содержащая только начальные буквы текстовых значений,
которые входят в список."""


class MyClass:
    def __init__(self, lst: list):
        self.lst = lst

    def __setattr__(self, key, value):
        if key == "lst" and isinstance(value, list):
            lst = [i for i in value if isinstance(i, str)]
            object.__setattr__(self, key, lst)

    def __getattribute__(self, item):
        if item == "lst":
            return ''.join([i[0] for i in object.__getattribute__(self, item)])


if __name__ == '__main__':
    obj = MyClass([1, "jhg", 2, "iuyt", 6, "edf"])
    print(obj.lst)
