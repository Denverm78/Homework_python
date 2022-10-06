# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

import random

def Get_random_polinomial(number_k):    # Создание случайного многочлена
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


def Get_polinomial(coef_list):
    my_list = coef_list[::-1]
    res_polinomial = ''
    for i in range(len(my_list)):
        if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
            res_polinomial += f'{abs(my_list[i])}x^{len(my_list)-i-1}'
            if my_list[i+1] != 0 or my_list[i+2] != 0:
                if my_list[i] > 0:
                    res_polinomial += ' + '
                else:
                    res_polinomial += ' - '   
        elif i == len(my_list) - 2 and my_list[i] != 0:
            res_polinomial += f'{abs(my_list[i])}x'
            if my_list[i+1] != 0 or my_list[i+2] != 0:
                if my_list[i] > 0:
                    res_polinomial += ' + '
                else:
                    res_polinomial += ' - '
        elif i == len(my_list) - 1 and my_list[i] != 0:
            res_polinomial += f'{abs(my_list[i])} = 0'
        elif i == len(my_list) - 1 and my_list[i] == 0:
            res_polinomial += ' = 0'
    return res_polinomial


def Write_polinominal_in_file(path_write, result): # Запись многочлена в файл
    try:
        with open (path_write, "w") as data:
            data.write(result)
    except:
        print("Ошибка работы с файлом")


def Read_polinominal_from_file(path_read): # Чтение многочлена из файла
    try:
        with open (path_read, "r") as data:
            pol_str = data.readlines()
            return pol_str
    except:
        print("Ошибка работы с файлом")


def Get_degree(my_polinominal): # Получение степени k многочлена
    if 'x^' in my_polinominal:
        i = my_polinominal.find('^')
        degree = int(my_polinominal[i+1:])
    elif ('x' in my_polinominal) and ('^' not in my_polinominal):
        degree = 1
    else:
        degree = -1
    return degree


def Get_coef(member): # Получение коэффициента перед членом многочлена
    if 'x' in member:
        i = member.find('x')
        temp_coef = member[:i-1]
        if temp_coef[0] == '+':
            temp_coef = temp_coef[1:]
            my_coef = int(temp_coef)
        elif temp_coef[0] == '-':
            temp_coef = temp_coef[1:]
            my_coef = (int(temp_coef))*(-1)
        else:
            my_coef = int(temp_coef)
    return my_coef


def Splitting_polinominal(polinominal): # Разбитие многочлена
    my_list = []
    polinominal = str(polinominal).split(" ")
    polinominal = polinominal[1:]
    polinominal = polinominal[:-2]
    new_polinominal = []
    new_polinominal.append(polinominal[0])
    i_new = 1
    while i_new < len(polinominal):
        new_polinominal.append(polinominal[i_new] + polinominal[i_new+1])
        i_new+=2
    lenght_pol = len(new_polinominal)
    coef = 0
    if Get_degree(new_polinominal[-1]) == -1:
        my_list.append(int(new_polinominal[-1]))
        coef = 1
        lenght_pol -= 1
    degree = 1 
    index_x = lenght_pol-1 
    while index_x >= 0:
        if Get_degree(new_polinominal[index_x]) != -1 and Get_degree(new_polinominal[index_x]) == degree:
            my_list.append(Get_coef(new_polinominal[index_x]))
            index_x -= 1
            degree += 1
        else:
            my_list.append(0)
            degree += 1
    return my_list

def Get_summ_pol_polinominal(pol_1, pol_2): # Получение суммы многочленов
    less_pol = len(pol_1)
    if len(pol_1) > len(pol_2):
        less_pol = len(pol_2)
    new_polinominal = [pol_1[i] + pol_2[i] for i in range(less_pol)]
    if len(pol_1) > len(pol_2):
        more_pol = len(pol_1)
        for i in range(less_pol,more_pol):
            new_polinominal.append(pol_1[i])
    else:
        more_pol = len(pol_2)
        for i in range(less_pol,more_pol):
            new_polinominal.append(pol_2[i])
    return new_polinominal

    

degree_k1 = int(input("Введите степень первого многочлена k1: "))
degree_k2 = int(input("Введите степень первого многочлена k2: "))
result1 = Get_random_polinomial(degree_k1)
result2 = Get_random_polinomial(degree_k2)
print(f"Полученный случайный многочлен 1: {result1}")
print(f"Полученный случайный многочлен 2: {result2}")
path_write_polinomial_1 = r"text5_1.txt"
path_write_polinomial_2 = r"text5_2.txt"
path_write_result = r"text5_res.txt"
Write_polinominal_in_file(path_write_polinomial_1, result1)
Write_polinominal_in_file(path_write_polinomial_2, result2)
path_read_polinomial_1 = r"text5_1.txt"
path_read_polinomial_2 = r"text5_2.txt"
polinomial_1_str = Read_polinominal_from_file(path_read_polinomial_1)
polinomial_2_str = Read_polinominal_from_file(path_read_polinomial_2)
list1 = Splitting_polinominal(polinomial_1_str)
list2 = Splitting_polinominal(polinomial_2_str)
summ_pol_polinomial = Get_summ_pol_polinominal(list1, list2)
res = Get_polinomial(summ_pol_polinomial)
print(f"Сумма двух многочленов: {res}")
Write_polinominal_in_file(path_write_result, res)
print(f"Первый многочлен записан в файл {path_read_polinomial_1}")
print(f"Второй многочлен записан в файл {path_read_polinomial_2}")
print(f"Сумма многочленов записана в файл {path_write_result}")
