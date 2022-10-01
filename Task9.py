# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# 0,56 -> 11

numberN = (input("Введите число N: "))
sum = 0
for digit in numberN:
    if digit.isdigit():
        sum += int(digit)
print(f"Сумма цифр в числе {numberN} равна {sum}")
