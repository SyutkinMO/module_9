# ------------Создание функций на лету------------


first = 'Мама мыла раму'
second = 'Рамена мало было'

from itertools import zip_longest

print(list(
    map(lambda x, y: list(i == j for i, j in (zip_longest(x.replace(' ', ''), y.replace(' ', '')))), first, second)))

itog = list((x == y) for x, y in (zip_longest(first.replace(' ', ''), second.replace(' ', ''))))
print(itog)


def func_(fir, sec):
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


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

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
