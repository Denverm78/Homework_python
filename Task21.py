# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N

numberN = int(input("Введите число: "))

i = 2 
result_list = []
temp = numberN

while i <= temp:
    if (temp % i) == 0:
        result_list.append(i)
        temp /= i
    else:
        i += 1
        
print(f"Простые множители числа {numberN}: {result_list}")
