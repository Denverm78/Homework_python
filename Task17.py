# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# 45 -> 101101
# 3 -> 11
# 2 -> 10
#     print(f"Число {num} в двоичной системе это {binum})

def convert_dec_to_bin(num_dec):
    binum = ""
    while num_dec > 0:
        binum = str(num_dec % 2) + binum
        num_dec = num_dec // 2
    return binum

num = int(input("Введите десятичное число: "))
binum = convert_dec_to_bin(num)
print(f"Число {num} в двоичной системе это {binum}")
