# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

number_n = float(input("Введите число: "))
first_digit = int(number_n * 10 % 10)
print(f"Первая цифра дробной части числа {number_n} - {first_digit}")
