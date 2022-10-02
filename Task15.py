# Напишите программу, которая найдёт произведение пар чисел списка
# (Список создаем как в предыдущем задании).
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
number = int(input("Введите число элементов списка: "))

def get_random_list(n):
    list1 = []
    for i in range(n):
        list1.append(random.randint(1, 10))
    return list1

def get_result_list(list1):
    list2 = []
    if (len(list1) % 2) == 0:
        middle_element = int(len(list1)/2)
    else:
        middle_element = int(len(list1)/2+1)
    print(middle_element)
    for i in range(middle_element):
        list2.append(list1[i]*list1[-1-i])
    return list2

my_list = get_random_list(number)
result_list = get_result_list(my_list)
print(f"Исходный список: {my_list}")
print(f"Получившийся список произведений пар чисел: {result_list}")
