# 3. Создайте программу для игры в 'Крестики-нолики'.

def Draw_square(square): # Рисуем поле для игры
        print()
        print (" ", square[0], "|", square[1], "|", square[2])
        print ("-------------")
        print (" ", square[3], "|", square[4], "|", square[5])
        print ("-------------")
        print (" ", square[6], "|", square[7], "|", square[8])

def Get_move_of_player(player): # Получаем ход игрока и отображаем на поле
    check = False
    while not check:
        print()
        move_of_player = int(input(f"Ход игрока {player}. Введите номер клетки: "))
        if (str(square[move_of_player-1]) != "O" and (str(square[move_of_player-1]) !="X")):
            square[move_of_player-1] = player
            check = True
        else:
            print ("Эта клетка уже занята")

def Check_of_win(square): # Проверяем выигрыш
    win_variant = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_variant:
        if square[i[0]] == square[i[1]] == square[i[2]]:
            return square[i[0]]
    return False


square = [1,2,3,4,5,6,7,8,9]
count = 0
win = False
while not win:
    Draw_square(square)
    if count % 2 == 0:
        Get_move_of_player("X")
    else:
        Get_move_of_player("O")
    count += 1
    pl = Check_of_win(square)
    if pl:
        print()
        Draw_square(square)
        print()
        print (f"Игра закончена, выиграл {pl} !\n")
        win = True
        exit()
    if count == 9:
        print()
        Draw_square(square)
        print()
        print ("Ничья!\n")
        exit()
