"""Напишите программу, в которой создается бинарное дерево объектов: в вершине структуры находится объект,
который содержит ссылки на два объекта того же класса. Каждый из этих объектов содержит ссылки на два объекта,
и так далее."""


class MyClass:
    def __init__(self, value, right=None, left=None):
        self.right = right
        self.left = left
        self.value = value


class Tree:

    def __init__(self, size: int):
        self.head = MyClass(0)
        self._build_tree(self.head, size)

    def _build_tree(self, obj: MyClass, size: int):
        if obj.value + 1 < size:
            obj.left = MyClass(obj.value + 1)
            self._build_tree(obj.left, size)
        if obj.value + 2 < size:
            obj.right = MyClass(obj.value + 2)
            self._build_tree(obj.right, size)


if __name__ == '__main__':
    tree = Tree(10)
