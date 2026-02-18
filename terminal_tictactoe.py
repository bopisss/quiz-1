board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw():
    return " " not in board

def play_game():
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are from 1 to 9 (left to right).")

    while True:
        print_board()
        move = input(f"Player {current_player}, choose a position (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Try again.")
            continue

        move = int(move) - 1

        if board[move] != " ":
            print("That spot is already taken. Try again.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()