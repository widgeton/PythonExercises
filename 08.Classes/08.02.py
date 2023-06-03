"""Напишите программу, в которой описан класс со следующими свойствами. В классе описан конструктор, которому
в качестве аргументов (помимо первой ссылки на создаваемый объект) передаются текст и целое число, причем
в произвольном порядке. Число и текст присваиваются как значения определенным полям. Если переданы два текстовых
значения, то создается только текстовое поле со значением, получающимся объединением значений аргументов.
Если аргументами переданы два числовых поля, то у объекта будет только поле с целочисленным значением, равным
сумме значений аргументов. В иных случаях поля для объекта не создаются. Создать на основе класса объекты и
проверить функциональность кода."""


class MyClass:
    def __init__(self, val1, val2):
        if (isinstance(val1, str) and isinstance(val2, str)) or \
                (isinstance(val1, int) and isinstance(val2, int)):
            self.value = val1 + val2
        elif (isinstance(val1, str) and isinstance(val2, int)) or \
                (isinstance(val1, int) and isinstance(val2, str)):
            self.val1 = val1
            self.val2 = val2


obj1 = MyClass("asdfg", "dfgh")
obj2 = MyClass("asdfg", 5)
obj3 = MyClass(5, 5)
obj4 = MyClass([6, 7, 8], 8)

print(obj1.value)
print(obj2.val1, obj2.val2)
print(obj3.value)
print(dir(obj4))
