# Реализуйте алгоритм перемешивания списка.

import random
kol_element = int(input("Введите количество элементов списка: "))
original_list = []
for i in range(kol_element):
    original_list.append(input(f"Введите {i+1}-й элемент: "))
print(f"Исходный список: {original_list}")

count = kol_element-1
result_list = []
while count >= 0:
    i = random.randint(0, count)
    result_list.append(original_list[i])
    original_list.pop(i)
    count -= 1
print(f"Новый перемешанный список: {result_list}")
