# ---------------Декораторы---------------


"""Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции
будет простым числом и "Составное" в противном случае."""


def is_prime(function):
    def wrapper(*args):
        result_ = function(*args)  # сохраняем результат работы декорируемой функции с переданными ей параметрами
        prime_ = ''
        for i in range(2, int(result_ ** 0.5) + 1):  # проверка на простоту
            if result_ % i == 0:
                prime_ = 'Составное'
            else:
                prime_ = 'Простое'
        print(prime_)
        return result_  # функция wrapper возвращает результат декорируемой функции

    return wrapper  # функция is_prime возвращает функцию wrapper


@is_prime  # декорирование
def sum_three(one, two, three):
    return one + two + three


result = sum_three(2, 3, 6)
print(result)
