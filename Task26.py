# 2. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# Человек против человека

from random import randint

def Get_first_player(play_1, play_2, col_cand):  # Выбираем случайную очередность
    rand_digit = randint(0, 1)
    if rand_digit == 0:
        print(f"Первым берет конфеты {play_1}. Всего на столе {col_cand} конфет")  # 0
    else:
        print(f"Первым берет конфеты {play_2}. Всего на столе {col_cand} конфет")  # 1
    return rand_digit


def Get_numbers_of_candies(player):
    col = int(input(f"{player}, сколько конфет вы возьмете? (число от 1 до 28) "))
    while col < 1 or col > 28:
        print("Вы ввели неверное число.")
        col = int(input("Введите правильное количество: "))
    return col


col_candies = 150
player1 = input("\nВведите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
priority = Get_first_player(player1, player2, col_candies)

while col_candies > 28:
    if priority == 0:
        k = Get_numbers_of_candies(player1)
        col_candies -= k
        priority = 1
    else:
        k = Get_numbers_of_candies(player2)
        col_candies -= k
        priority = 0
    print(f"Осталось {col_candies} конфет")

if priority == 0:
    print(f"Выиграл {player1}, он забирает все конфеты")
else:
    print(f"Выиграл {player2}, он забирает все конфеты\n")
