"""Напишите программу, в которой создается цепочка объектов. Предложите метод или функцию, которые позволяют
вставить новый объект в уже существующую цепочку, а также метод или функцию, которые позволяют удалить объект
из цепочки (так, чтобы оставшиеся объекты образовали цепочку)."""


class MyClass:
    def __init__(self, value, nxt=None):
        self.nxt = nxt
        self.value = value


class Chain:
    def __init__(self, size: int):
        self.first = MyClass(0)
        cur = self.first
        for i in range(1, size + 1):
            cur.nxt = MyClass(i)
            cur = cur.nxt

    def _find(self, spot: int) -> MyClass:
        cur = self.first
        for _ in range(spot - 2):
            cur = cur.nxt
            if cur.nxt.nxt is None:
                break
        return cur

    def show(self):
        cur = self.first
        while cur.nxt is not None:
            print(cur.value, end=" -> ")
            cur = cur.nxt
        print("None")

    def insert(self, spot: int, value):
        cur = self._find(spot)
        if cur.nxt is not None:
            inserted = MyClass(value)
            nxt = cur.nxt
            cur.nxt = inserted
            inserted.nxt = nxt
        else:
            cur.nxt = MyClass(value)

    def remove(self, spot: int):
        cur = self._find(spot)
        if cur.nxt.nxt is not None:
            cur.nxt = cur.nxt.nxt


if __name__ == '__main__':
    chain = Chain(10)
    chain.show()
    chain.insert(6, 24)
    chain.show()
    chain.remove(6)
    chain.show()
