#! /usr/bin/env python
# -*- coding: utf-8 -*-

#  Игра в "Крестики - Нолики"
#  Правила
#  1. Игрок вводит координаты следующего хода
#  2. Программа "отрисовывает" ход и предлагает сделать ход следующему игроку
#  3. Если один из игроков заполняет линию своим символом по горизонтале, вертикале или диагонале, он "Выигрывает"
#  4. Если ни один игрок не заполняет своим символом прямую линию из 3- х символов, то -  "Ничья"
#  Целевая картинка:
#          0 1 2
#        0 x x 0
#        1 - - 0
#        2 x 0 x

# функция печати игрового поля
def print_matix(pf):
    # создадим полное игровое поле, добавим координаты
    full_pf = []
    for i in range(4):
        if i == 0:
            full_pf.append([' ', '0', '1', '2'])
        else:
            str_ = str(i-1) + "".join(list(map(str, pf[i-1])))  # построим новую строку с координатой
            full_pf.append(list(str_))  # добавим новую строку в полное игровое поле
    for i in range(4):
        print(f"""{" ".join(list(map(str, full_pf[i])))}""")


#  функция проверки вводимых значений координат
def right_enter(str_):
    if str_ is None:
        return False
    if len(str_) != 3:
        print('Координаты хода не соответствуют формату. Строка не из 3-х символов')
        return False
    elif not str_[0].isdigit() or not str_[2].isdigit():
        print('Координаты хода не соответствуют формату. Координаты не цифры')
        return False
    elif all([(0 <= int(str_[0]) <= 2),
              (str_[1] == ' '),
              (0 <= int(str_[2]) <= 2)]):
        return True
    else:
        print('Координаты хода не соответствуют формату. Формат ввода: Цифра Пробел Цифра. Цифра от 0 до 2')
        return False


#  функция определения - а не кончилась ли игра? вход - игровое поле и текущий игрок
def end_game(field_game, cur_p):
    sum_count = [0, 0, 0, 0, 0, 0, 0, 0]   # для хранения сумм по строкам (0-2) колонкам (3-5) и диагоналям (6-7)

    # преобразуем игровое поле в числовую таблицу
    dig_matrix = []
    for i in range(3):
        dig_matrix.append([0 if x == '0' else 1 if x == 'x' else 4 for x in field_game[i]])

    # посчитаем значения по строкам, столбцам и диагоналям и сохраним в список сумм
    for i in range(3):
        for j in range(3):
            sum_count[i] += dig_matrix[i][j]
            sum_count[j+3] += dig_matrix[i][j]
            if i == j:
                sum_count[6] += dig_matrix[i][j]
            if (i == j == 1) or (i == 0 and j == 2) or (i == 2 and j == 0):
                sum_count[7] += dig_matrix[i][j]

    # все ходы кончились - ничья
    if all([x < 3 for x in sum_count]):
        print(f'Игра окончена. Ничья')
        return True

    if (any([x in [0, 3] for x in sum_count]) and cur_p == 'x') or all([x <= 3 for x in sum_count]):  # проверим список сумм на наличие выйгрышей
        if len(list(filter(lambda x: x == 0, sum_count))) == len(list(filter(lambda y: y == 3, sum_count))):
            print(f'Игра окончена. Ничья')
        elif len(list(filter(lambda x: x == 0, sum_count))) > len(list(filter(lambda y: y == 3, sum_count))):
            print(f'Игра окончена. Выиграл игрок "0"')
        elif len(list(filter(lambda x: x == 0, sum_count))) < len(list(filter(lambda y: y == 3, sum_count))):
            print(f'Игра окончена. Выиграл игрок "X"')
        return True

    return False

# Основной скрипт
# создаем поле для игры
play_field = [['-' for j in range(3)] for i in range(3)]
print_matix(play_field)

cur_hod = None
player = 'x'  # текущий игрок

while not end_game(play_field, player):
    while not right_enter(cur_hod):
        cur_hod = input(f'Введите координаты хода игрока "{player.upper()}" через пробел (пример: 1 2): ')

    if play_field[int(cur_hod[0])][int(cur_hod[2])] == '-':
        play_field[int(cur_hod[0])][int(cur_hod[2])] = player
        player = '0' if player == 'x' else 'x'
        print_matix(play_field)
        cur_hod = None
    else:
        print(f'Поле c координатами: {cur_hod} занято.')
        cur_hod = None

