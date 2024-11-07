# -----------"Списковые, словарные сборки"-----------


first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

"""
В переменную first_result запишите список, созданный при помощи сборки 
состоящий из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.
"""

first_result = [len(i) for i in first_strings if len(i) >= 5]
print(first_result)

"""
В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины. 
Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
"""

second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]
print(second_result)

"""
В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет 
строка-длина строки. Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings. 
Условие записи пары в словарь - чётная длина строки.
"""

third_result = [{word: len(word)} for word in (first_strings + second_strings) if len(word) % 2 == 0]
print(third_result)