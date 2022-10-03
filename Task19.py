# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
# псевдослучайных чисел. БЕЗ КАКИХ ЛИБО РАНДОМОВ

# Программа выдает псевдослучайное число от 10 до 99

import time


def random_number():
    a1 = (time.time())
    time.sleep(0.5)
    a2 = (time.time())
    a1 = a1*10000000 % 1000
    a2 = a2*10000000 % 1000
    a = (a1/a2)*10
    while a >= 100:  # Максимальное значение
        a /= 10
    if a < 10:       # Минимальное значение
        a *= 10
    return int(a)


print(random_number())
print(random_number())
print(random_number())
print(random_number())
print(random_number())
