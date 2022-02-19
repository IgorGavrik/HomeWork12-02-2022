# # 1. Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# # это порядковый номер строки в списке. Использовать генератор списков.
# n = (int(input("Введите размерность списка: ")))
# b = [str(input("Введите строку списка: ")) for _ in range(n)]
# print(f"\n"
#       f"Дан список строк: {b}\n"
#       f"")
# a = [i for i in range(len(b)+1) if i>0]
# c = []
# for i in range(len(b)):
#     c.append(str(a[i])+'-'+str(b[i]))
# print(f'Новый список с порядковым номером каждой строки \n'
#       f'{c}\n'
#       f'Прошу подтвердить правильность выполнения задания.')

# # 2. Создать lambda функцию, которая принимает на вход неопределенное
# # количество именных аргументов и выводит словарь с ключами удвоенной
# # длины. {‘abc’: 5} -> {‘abcabc’: 5}
# # https://webdevblog.ru/kak-perebrat-slovar-v-python/ Отличная статья
# # по перебиранию словарей
# # https://webdevblog.ru/kak-ispolzovat-v-python-lyambda-funkcii/ И по Lambda
# n = (int(input("Введите размерность словаря (цифрой): ")))
# a_keys = [input(f"Введите ключ {i+1} словаря: ") for i in range(n)]
# a_values = [input(f"Введите значение {i+1} ключа: ") for i in range(n)]
# a = {key: value for key,value in zip(a_keys,a_values)}
# b = lambda **kwargs: {key+key:value for key,value in a.items()}
# print(f"\nПервоначальный словарь\n {a}\n")
# print(f"Модифицированный словарь\n {b()}")

# 3. Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.
# def num_a():
#     n = random.randrange(2, 9, 1)
#     print(f"Длина списка случайным выбором равна: {n}")
#     a = [int(input(f"Введите число №{i+1}: ")) for i in range(n)]
#     print(f"\nПолучен список чисел\n{a}\n")
#     return a
# def modify(num_a):
#     print("Принимаем список чисел")
#     b = num_a()
#     c = []
#     for i in b:
#         if (i%2)>0:
#             c.append(i)
#         elif (i%2)==0:
#             continue
#     print(f"Список без чётных элементов списка:\n{c}")
# import random
# modify(num_a)

# 4. Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.
# Отличная статья про циклы https://breakingcode.ru/krasivyy-python-chast-1-pravilnye-cikly-v-python/
def num_a():
    n = random.randrange(2, 9, 1)
    print(f"Длина списка случайным выбором равна: {n}")
    a = [random.randrange(1, 10, 1) for i in range(n)]
    print(f"\nПолучен список чисел\n{a}\n")
    return a
def modify(num_a):
    print("Принимаем список чисел")
    b = num_a()
    c = []
    for i in reversed(b):
        c.append(i)
    print(f"Спиcок в обратную сторону:\n{c}")
import random
modify(num_a)
