

import chess

def print_board(board):
    print(board)
    print('\n')

def play_game():
    board = chess.Board()
    print_board(board)
    while not board.is_game_over():
        try:
            move = input("Enter your move in UCI format (e.g. e2e4): ")
            board.push(chess.Move.from_uci(move))
            print_board(board)
        except ValueError:
            print("Xato urinish bo'ldi, qaytadan urinib ko'ring!")
    result = board.result()
    if result == '1-0':
        print("White wins!")
    elif result == '0-1':
        print("Black wins!")
    else:
        print("Draw!")

if __name__ == '__main__':
    play_game()