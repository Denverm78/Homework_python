#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
#координат точек в этой четверти (x и y).

number_quarter = int(input("Введите номер четверти координатной плоскости: "))
if number_quarter < 1 or number_quarter > 4:
    print("Вы ввели неверный номер четверти (введите 1,2,3 или 4)")
if number_quarter == 1:
    print(f"В четверти {number_quarter} координаты точки: x > 0 и y > 0")
if number_quarter == 2:
    print(f"В четверти {number_quarter} координаты точки: x < 0 и y > 0")
if number_quarter == 3:
    print(f"В четверти {number_quarter} координаты точки: x < 0 и y < 0")
if number_quarter == 4:
    print(f"В четверти {number_quarter} координаты точки: x > 0 и y < 0")

