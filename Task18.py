# 5. Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def positive_fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return positive_fibonacci(n - 1) + positive_fibonacci(n - 2)

def negative_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (negative_fibonacci(n-2) - negative_fibonacci(n-1))

number = int(input("Введите число: "))
pos_fib = []
neg_fib = []

for i in range(1, number):
    pos_fib.append(positive_fibonacci(i))

for j in range(0, number):
    neg_fib.append(negative_fibonacci(j))
neg_fib = list(reversed(neg_fib))

result = neg_fib + pos_fib
print(f"Список чисел Фибоначчи для числа {number} - {result}")
