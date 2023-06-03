"""Напишите программу, в которой методом рекурсии вычисляется сумма геометрической
прогрессии: первое слагаемое равно единице, а каждое следующее получается из предыдущего
умножением на определенное число (передается в качестве аргумента функции, также как
и количество слагаемых в сумме)."""


def geometric_progression(factor, amount, start=1):
    if amount < 1:
        return 0
    return start + geometric_progression(factor, amount - 1, start * factor)


print(geometric_progression(2, 5))

