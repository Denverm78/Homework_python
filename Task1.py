# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

number_n = int(input("Введите число N: "))
for i in range(-number_n, number_n):
    print(i, end=', ')
print(number_n)
