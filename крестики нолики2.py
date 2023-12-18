"""крестики нолики """

"""Создание игрового поля"""
game_board = [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']]

"""Отображение игрового поля"""
def output_game_board (board):
    for i in board:
        for j in i:
            print(j, end=' ')
        print('\n ')
output_game_board(game_board)


"""Проверка победы"""
def  win_game(board, player):
    for i in board:
        if i.count(player) == 3:
            return True
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[2][0] == board[1][1] == board[0][2] == player:
            return True
    return False

"""Запуск игры"""
"""Основная программа"""
player = 'X'
while True:
    output_game_board(game_board)
    print(f"Ходит игрок {player}")
    i = int(input("Введите номер строки: ")) - 1
    j = int(input("Введите номер столбца: ")) - 1
    if game_board[i][j] != '_':
        print('Ячейка занета')
        continue
    game_board[i][j] = player
    if win_game(game_board, player):
        output_game_board(game_board)
        print(f'Игрок {player} Выиграл')
        break
    player = '0' if player == 'X' else "X"