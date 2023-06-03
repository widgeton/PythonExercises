"""Напишите программу, в которой создается функция с двумя аргументами,
являющимися числовыми списками. Результатом является число, равное сумме
попарных произведений элементов списков. Если в одном из списков элементов
меньше, чем в другом, то недостающие элементы получают путем циклического
повторения содержимого списка."""


def sum_values_of_lists(lst1: list[int], lst2: list[int]) -> list[int]:
    lst = []
    for i in range(max(len(lst1), len(lst2))):
        if i > len(lst1) - 1:
            lst.append(lst2[i] + lst1[i - len(lst1)])
        elif i > len(lst2) - 1:
            lst.append(lst1[i] + lst2[i - len(lst2)])
        else:
            lst.append(lst1[i] + lst2[i])
    return lst


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(sum_values_of_lists(list1, list2))
   