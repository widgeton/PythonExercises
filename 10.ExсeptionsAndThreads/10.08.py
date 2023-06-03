"""Напишите программу, в которой создается объект с двумя списками. Списки заполняются
значениями с помощью двух дочерних потоков: один список заполняется символами, а второй
список заполняется числами."""
from threading import Thread


class MyClass:
    def __init__(self):
        self.lst1 = []
        self.lst2 = []

    def fill_lst1(self, size):
        lit = ord('a')
        for i in range(size):
            self.lst1.append(chr(lit + i))

    def fill_lst2(self, size):
        for i in range(size):
            self.lst2.append(i)


if __name__ == '__main__':
    obj = MyClass()
    t1 = Thread(target=obj.fill_lst1, args=(8,))
    t2 = Thread(target=obj.fill_lst2, args=(8,))

    t1.start()
    t2.start()

    if t1.is_alive():
        t1.join()

    if t2.is_alive():
        t2.join()

    print(obj.lst1)
    print(obj.lst2)
