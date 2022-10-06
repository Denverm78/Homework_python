# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# Решил двумя способами после мучений с округлением :)

# list = '3.1415926535897932'

# tochnost = float(input("Введите точность для числа Пи (от 0.1 до 0.0000000001): "))
# count = 0
# numberT = tochnost
# while numberT != 1:
#     numberT *= 10
#     count += 1

# result = ""

# for i in range(count+2):
#     result = result + list[i]

# result = float(result)
# print(f"Число Пи с точностью {tochnost} равно {result}")

import math

tochnost = float(input("Введите точность для числа Пи (от 0.1 до 0.0000000001): "))
count = 0
i = 10

while (tochnost * i) // 10 < 1:
    i *= 10
    count += 1

result = (int ((math.pi) * (10**count))) / (10**count)
print(f"Число Пи с точностью {tochnost} равно {result}")