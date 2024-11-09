# ---------------------Генераторные сборки---------------------


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

"""
Необходимо создать 2 генераторных сборки:
В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков
first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.

В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк 
в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. 
Используйте функции range и len.
"""

first_result = (len(i[0]) - len(i[0 + 1]) for i in (list(zip(first, second))) if len(i[0]) != len(i[0 + 1]))
print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))
print(list(second_result))
