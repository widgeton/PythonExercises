"""Напишите программу с классом, объекты которого можно вызывать. У объекта класса должно быть поле-список
с числовыми значениями, а результатом метод возвращает полиномиальную сумму. В частности, если в списке
содержатся числа a0, a1, …, an и в качестве аргумента объекту при вызове передается значение x, то в качестве
результата должно возвращаться значение a0 + a1*x + a2*x^2 + … + an*x^n."""


class MyClass:
    def __init__(self, lst: list):
        self.lst = lst

    def __call__(self, x):
        return sum([i * (x ** j) for j, i in enumerate(self.lst)])


if __name__ == '__main__':
    obj = MyClass([1, 2, 3, 4])
    print(obj(2))