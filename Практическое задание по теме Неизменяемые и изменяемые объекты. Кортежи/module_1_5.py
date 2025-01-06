# Ваша задача:
# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
#
#
#
# Цель:
#
# Написать программу на языке Python, используя Pycharm, для работы с неизменяемыми и изменяемыми объектами.
#
#
#
# 1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_5.py' и напишите весь код в нём.
#
#
#
# 2. Задайте переменные разных типов данных:
#
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
#
#   - Выполните операции вывода кортежа immutable_var на экран.
#
#
#
# 3. Изменение значений переменных:
#
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#
#
#
# 4. Создание изменяемых структур данных:
#
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#
#   - Измените элементы списка mutable_list.
#
#   - Выведите на экран измененный список mutable_list.
#
#
#
# Примечания:
#
# - Для вывода значений на экран используйте функцию print().
#
# - Обратите внимание на особенности изменяемых и неизменяемых объектов в Python.
#
#
#
# Пример результата выполнения программы:
#
# Immutable tuple: (1, 2, 'a', 'b')
#
# Mutable list: [1, 2, 'a', 'b', 'Modified']
#
#
#
# Напишите код к домашнему заданию в ответе (комментарии).
#
#
#
# Успехов! #


# Solution

immutable_var = (1, True, 'a', 3.14)
print(immutable_var)

# immutable_var[0] = 2 Can't to change values inside a tuple
# print(immutable_var) Tuple is an immutable object in Python

mutable_list = [2, False, 'b', 1.99]
print(mutable_list)
mutable_list[1] = True
print(mutable_list)