# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

numberN = int(input("Введите число N: "))
result = []
mult = 1
for i in range(1, numberN+1):
    mult *= i
    result.append(mult)
print(f"Набор произведений чисел от 1 до {numberN}: {result}")
