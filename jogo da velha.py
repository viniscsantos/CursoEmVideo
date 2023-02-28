def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def check_win(board, player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False

def main():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    current_player = players[0]
    game_over = False

    while not game_over:
        print_board(board)
        move = int(input("Player " + current_player + ", enter your move (0-8): "))

        if board[move] == " ":
            board[move] = current_player
            if check_win(board, current_player):
                print_board(board)
                print("Congratulations, Player " + current_player + " wins!")
                game_over = True
            elif " " not in board:
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = players[1] if current_player == players[0] else players[0]
        else:
            print("That space is already taken. Please try again.")

if __name__ == "__main__":
    main()
