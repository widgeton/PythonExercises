"""Напишите программу для вычисления множества чисел (в пределах
первой полусотни), которые делятся или на 3, или на 4, но при этом
не делятся одновременно на 3 и 4."""

three_divider_set = {i for i in range(50) if i % 3 == 0}
four_divider_set = {i for i in range(50) if i % 4 == 0}

result = three_divider_set ^ four_divider_set

print(result)
