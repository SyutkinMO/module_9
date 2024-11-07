# ------------Введение в функциональное программирование------------


def apply_all_func(int_list, *functions) -> dict:
    """
     Функция apply_all_func(int_list, *functions), которая принимает параметры:
    :param int_list: список из чисел (int, float)
    :param functions: неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
    :return: словарь, где ключом будет название вызванной функции,
            а значением - её результат работы со списком int_list.
    """
    results = {}
    for i in functions:
        results[i.__name__] = i(int_list)
    return results


def min_(*args):
    return min(*args)


def max_(*list):
    return max(*list)


def len_(*list):
    return len(*list)


def sum_(*list):
    return sum(*list)


def sorted_(*list):
    return sorted(*list)


print(apply_all_func([6, 20, 15, 9], max_, min_))
print(apply_all_func([6, 20, 15, 9], len_, sum_, sorted_))
