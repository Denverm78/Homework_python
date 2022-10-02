# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# ВАЖНО: если число целое, то оно не имеет дробной части и засчитывать 0 как минимальное не стоит
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def get_my_list(number_element):
    list1 = []
    for i in range(number_element):
        list1.append(float(input(f"Введите {i+1}-й элемент: ")))
    return list1

def find_difference(list2):
    max_value = round(list2[0] % 1, 5)
    min_value = round(list2[0] % 1, 5)
    for i in list2:
        value = round(i % 1, 5)
        if value < min_value and value != 0:
            min_value = value
        if value > max_value and value != 0:
            max_value = value
    result = max_value - min_value
    return result

kol_element = int(input("Введите количество элементов списка: "))
my_list = get_my_list(kol_element)
difference = find_difference(my_list)
print(f"Разница между max и min значением дробной части элементов списка {my_list} равна {difference}")
