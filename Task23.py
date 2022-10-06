# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random

def Get_polinomial(number_k): # Создание случайного многочлена
    list_coef = []  # Случайные коэффициенты
    for i in range(number_k+1):
        list_coef.append(random.randint(0, 100))

    list_sign = []  # Случайные знаки
    for i in range(number_k):
        if (random.randint(0, 1)) == 0:
            list_sign.append("-")
        else:
            list_sign.append("+")

    result = ""
    for i in range(number_k-1):
        if list_coef[i] != 0:
            result = result + f" {list_coef[i]}*x^{number_k-i} {list_sign[i]}"

    if list_coef[number_k-1] != 0:
        result = result + f" {list_coef[number_k-1]}*x "

    if list_coef[number_k] != 0:
        result = result + f"{list_sign[number_k-1]} {list_coef[number_k]} = 0"
    else:
        result = result + " = 0"
    
    return(result)

def Write_polinominal_in_file(path_write, result): # Запись многочлена в файл
    try:
        with open (path_write, "w") as data:
            data.write(result)
    except:
        print("Ошибка работы с файлом")

def Read_polinominal_from_file(path_read): # Чтение многочлена из файла
    try:
        with open (path_read, "r") as data:
            data.read(result)
    except:
        print("Ошибка работы с файлом")     

degree_k = int(input("Введите степень k: "))
result_polinominal = Get_polinomial(degree_k)
print(f"Полученный случайный многочлен: {result_polinominal}")
path_write_result = r"text4.txt"
Write_polinominal_in_file(path_write_result, result_polinominal)
print(f"Полученный многочлен записан в файл {path_write_result}")
