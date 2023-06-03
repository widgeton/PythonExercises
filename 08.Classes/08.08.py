"""Напишите программу, в которой создается цепочка объектов. Для создания цепочки объектов предложите функцию,
при вызове которой в качестве аргумента передается целое число, определяющее количество объектов в цепочке.
Результатом функция должна возвращать ссылку на первый объект в цепочке."""


class MyClass:
    def __init__(self, value, nxt=None):
        self.nxt = nxt
        self.value = value


def get_chain(size: int) -> MyClass:
    first = MyClass(0)
    cur = first
    for i in range(1, size + 1):
        cur.nxt = MyClass(i)
        cur = cur.nxt
    return first


if __name__ == '__main__':
    obj = get_chain(10)
    while obj.nxt is not None:
        print(obj.value, end=" ")
        obj = obj.nxt
