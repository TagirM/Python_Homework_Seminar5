# 3. Создайте программу для игры в ""Крестики-нолики"".

def draw_board(board):
    print('-' * 50)
    for i in range(3):
        print(
            f'|\t{board[0 + i * 3]}\t|\t{board[1 + i * 3]}\t|\t{board[2 + i * 3]}\t|')
        print('-' * 50)


def take_input(player_token, board):
    valid = False
    while not valid:
        player_answer = input(
            f'Куда поставим {player_token}? Введите число 1 - 9: ')
        try:
            player_answer = int(player_answer)
        except:
            print('Некорректный ввод. Вы уверены, что ввели число?')
            continue
        if 1 <= player_answer <= 9:
            if (str(board[player_answer - 1]) not in 'XO'):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print('Эта клетка уже занята!')
        else:
            print('Некорректный ввод. Введите число от 1 до 9')


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X', board)
        else:
            take_input('0', board)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                draw_board(board)
                print(tmp, 'выиграл!')
                win = True
                break
        if counter == 8:
            draw_board(board)
            print('Ничья!')
            win = True
            break


def task3():
    print(f'{"*" * 10} Игра крестики-нолики для двух игроков {"*" * 10}')
    board = [i for i in range(1, 10)]
    main(board)


task3()
