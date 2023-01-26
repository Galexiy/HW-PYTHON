# Домашняя работа №5

# Игра крестики нолики с Ботом

# board = [' ' for x in range(9)]

# def print_board():
#     row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
#     row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
#     row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

#     print('-------------')
#     print(row1)
#     print('-------------')
#     print(row2)
#     print('-------------')
#     print(row3)
#     print('-------------')

# def player_move(icon):
#     choice = int(input('Ходите от 1 до 9: ').strip())
#     if board[choice - 1] == ' ':
#         board[choice - 1] = icon
#     else:
#         print()
#         print('Это место занято!')

# def is_victory(icon):
#     if (board[0] == icon and board[1] == icon and board[2] == icon) or \
#        (board[3] == icon and board[4] == icon and board[5] == icon) or \
#        (board[6] == icon and board[7] == icon and board[8] == icon) or \
#        (board[0] == icon and board[3] == icon and board[6] == icon) or \
#        (board[1] == icon and board[4] == icon and board[7] == icon) or \
#        (board[2] == icon and board[5] == icon and board[8] == icon) or \
#        (board[0] == icon and board[4] == icon and board[8] == icon) or \
#        (board[2] == icon and board[4] == icon and board[6] == icon):
#         return True
#     else:
#         return False

# def is_draw():
#     if ' ' not in board:
#         return True
#     else:
#         return False

# def bot_move(icon):
#     print('Ход Бота')
#     best_score = None
#     for i in range(len(board)):
#         if board[i] == ' ':
#             board[i] = icon
#             if icon == 'O':
#                 score = minimax('X', False)
#             else:
#                 score = minimax('O', False)
#             board[i] = ' '
#             if best_score == None or (icon == 'O' and score > best_score) or (icon == 'X' and score < best_score):
#                 best_score = score
#                 best_move = i
#     board[best_move] = icon

# def minimax(icon, is_maximizing):
#     if is_victory('X'):
#         return -1
#     elif is_victory('O'):
#         return 1
#     elif is_draw():
#         return 0

#     if is_maximizing:
#         best_score = None
#         for i in range(len(board)):
#             if board[i] == ' ':
#                 board[i] = 'O'
#                 score = minimax('X', False)
#                 board[i] = ' '
#                 if best_score == None or score > best_score:
#                     best_score = score
#         return best_score

#     else:
#         worst_score = None
#         for i in range(len(board)):
#             if board[i] == ' ':
#                 board[i] = 'X'
#                 score = minimax('O', True)
#                 board[i] = ' '
#                 if worst_score == None or score < worst_score:
#                     worst_score = score
#         return worst_score
# while True:
#     print_board()
#     player_move('X')
#     if is_victory('X'):
#         print_board()
#         print('X - побеждает! Поздравляю!')
#         break
#     elif is_draw():
#         print_board()
#         print('Ничья!')
#         break
#     bot_move('O')
#     if is_victory('O'):
#         print_board()
#         print('Бот выйграл! Тебе повезет следующий раз!')
#         break
