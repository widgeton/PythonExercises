"""Напишите программу, в которой, по аналогии с примером из листинга 10.8, с использованием
пользовательского класса исключения и рекурсивного вызова функции создается объект исключения
со списком, содержащим (в обратном порядке) буквы алфавита.
Листинг 10.8:

class MyError(Exception):
    def __init__(self):
        self.values=[]

    def __add__(self, val):
        self.values.append(val)
        return self

def getMyError(n):
    try:
        if n<=1:
            raise MyError
        getMyError(n-1)
    except MyError as error:
        raise error+n

def getList(n):
    try:
        getMyError(n)
    except MyError as error:
        return error.values

A=getList(10)
print(A)
B=getList(7.5)
print(B)
"""


class MyError(Exception):
    def __init__(self):
        self.values = []

    def __add__(self, val):
        self.values.append(val)
        return self


def get_MyError(n):
    try:
        if n >= 'я':
            raise MyError
        get_MyError(chr(ord(n) + 1))
    except MyError as error:
        raise error + n


def get_list(n='а'):
    try:
        get_MyError(n)
    except MyError as error:
        return error.values


if __name__ == '__main__':
    lst = get_list()
    print(lst)
