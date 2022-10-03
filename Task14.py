#  Задайте рандомно список из чисел размером N, где N число с клавиатуры.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  *Пример:*
#  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
number = int(input("Введите число элементов списка: "))

def get_random_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, 10))
    return list

def get_sum_odd_element(list):
    sum_odd_element = 0
    for i in range(1, len(list), 2):
        sum_odd_element += list[i]
    return sum_odd_element

my_list = get_random_list(number)
result = get_sum_odd_element(my_list)
print(f"Сумма элементов на нечетных позициях списка {my_list} равна {result}")
