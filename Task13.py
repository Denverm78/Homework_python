# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# 0,56 -> 11

numberN = float(input("Введите число N: "))
temp = 1
numberN = abs(numberN)
while temp > 0:
    numberN = round(numberN*10, 4)
    temp = numberN % 10

numberN = int(numberN/10)
sum = 0

while numberN > 1:
    sum = sum + int(numberN % 10)
    numberN /= 10

print(sum)
