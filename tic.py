import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                moves.append((i, j))
    return moves

def ai_move(board):
    # AI makes a random move
    moves = available_moves(board)
    return random.choice(moves)

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = move // 3, move % 3
            if board[row][col] not in ['X', 'O']:
                return row, col
            else:
                print("This cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please choose a number between 1 and 9.")

def tic_tac_toe():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, the AI is O.")
    
    while True:
        print_board(board)
        
        # Player's move
        row, col = player_move(board)
        board[row][col] = "X"

        if check_win(board, "X"):
            print_board(board)
            print("You win!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI's move
        print("AI's move:")
        row, col = ai_move(board)
        board[row][col] = "O"

        if check_win(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

tic_tac_toe()
