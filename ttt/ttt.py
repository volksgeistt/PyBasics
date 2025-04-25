def print_board(board):
    """Print the Tic-Tac-Toe board."""
    print("\nBoard:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9) 

def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def play_tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)] 
    current_player = "X"

    while True:
        print_board(board)
        print(f"\nPlayer {current_player}'s turn:")
        
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("Spot taken! Try again.")
                continue
            
        except ValueError:
            print("Please enter valid numbers (0, 1, or 2).")
            continue
        
        board[row][col] = current_player

        if check_win(board):
            print_board(board)
            print(f"\n🎉 Player {current_player} wins! 🎉")
            break

        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("\nIt's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

play_tic_tac_toe()
