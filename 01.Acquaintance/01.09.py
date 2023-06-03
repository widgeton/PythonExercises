"""Напишите программу, в которой описана функция, возвращающая результатом
второе по величине число в списке, переданном функции в качестве аргумента."""


def get_second_biggest_num(lst: list[int]) -> int:
    if lst[0] > lst[1]:
        max_num = lst[0]
        second_biggest_num = lst[1]
    else:
        max_num = lst[1]
        second_biggest_num = lst[0]

    for i in lst:
        if i > max_num:
            second_biggest_num, max_num = max_num, i

    return second_biggest_num


nums = [7, 6, 4, 8, 9, 3, 1]
print(get_second_biggest_num(nums))
