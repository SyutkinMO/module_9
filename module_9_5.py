# ----------------Итераторы----------------

class StepValueError(ValueError):  # пользовательский класс исключения StepValueError, который наследуется от ValueError
    pass


""" класс Iterator, который обладает следующими свойствами:
Атрибуты объекта:
start - целое число, с которого начинается итерация.
stop - целое число, на котором заканчивается итерация.
step - шаг, с которым совершается итерация.
pointer - указывает на текущее число в итерации (изначально start)
Методы:"""


class Iterator:

    def __init__(self, start, stop, step=1):
        """Метод __init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага.
        В этом методе в первую очередь проверяется step на равенство 0. Если равно, то выбрасывается исключение
         StepValueError('шаг не может быть равен 0')"""
        self.start = start  # start - целое число, с которого начинается итерация.
        self.stop = stop  # stop - целое число, на котором заканчивается итерация.
        self.step = step  # step - шаг, с которым совершается итерация.
        self.pointer = start  # pointer - указывает на текущее число в итерации (изначально start)
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        """__iter__ - метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора."""
        self.pointer = self.start
        return self

    def __next__(self):
        """__next__ - метод, увеличивающий атрибут pointer на step. В зависимости от знака атрибута
        step итерация завершится либо когда pointer станет больше stop, либо меньше stop."""
        if self.step < 0:
            if self.pointer < self.stop:
                raise StopIteration
            self.pointer += self.step
            return self.pointer - self.step
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration
            self.pointer += self.step
            return self.pointer - self.step


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)  # Класс создается, но итерация сразу заканчивается,
# так как start > stop и шаг по умолчанию + 1


for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')  # итерация сразу заканчивается, так как start > stop и шаг по умолчанию + 1
