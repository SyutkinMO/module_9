# ------------Создание функций на лету------------

"""Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
Здесь ? - место написания lambda-функции.
Результатом должен быть список совпадения букв в той же позиции"""

first = 'Мама мыла раму'
second = 'Рамена мало было'

list_bool = list(map(lambda x, y: x == y, first, second))
print(list_bool)  # в данном случае будут учитываться пробелы, и сравнение по наиболее короткой строке

from itertools import zip_longest

itog = list((x == y) for x, y in (zip_longest(first.replace(' ', ''), second.replace(' ', ''))))
print(itog)  # здесь выполнено удаление пробелов и недостающие буквы в более короткой строке будут заполнены None


def func_(fir, sec):  # вариант в виде функции
    list_ = []
    for x, y in zip_longest(fir.replace(' ', ''), sec.replace(' ', '')):
        list_.append(x == y)
    return list_


print(func_(first, second))


def get_advanced_writer(file_name):
    file = open(f'{file_name}', 'w+', encoding='utf-8')

    def write_everything(*data_set):
        for i in data_set:
            file.write(f'{i}\n')
        file.close()
        return

    return write_everything


"""Замыкание:
Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр,
принимающий неограниченное количество данных любого типа.
Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
Функция get_advanced_writer возвращает функцию write_everything."""

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

"""Метод __call__:
Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words и возвращать его. 
Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции функция choice из модуля random.
"""

import random


class MysticBall:
    words = []

    def __init__(self, *word):
        for i in word:
            self.words.append(i)

    def __call__(self):
        return random.choices(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
