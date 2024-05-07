import random

# Initialize the board
board = ["-" for _ in range(9)]

# Define the current player and winner
currentPlayer = "O"
winner = None

# Function to print the game board
def printBoard():
    print("")
    print(f"                             " + board[0] + " | " + board[1] + " | " + board[2])
    print("                             ---------")
    print(f"                             " + board[3] + " | " + board[4] + " | " + board[5])
    print("                             ---------")
    print(f"                             " + board[6] + " | " + board[7] + " | " + board[8])
    print("")

# Function to check for a win
def checkWin(player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                        (0, 4, 8), (2, 4, 6)]  # Diagonals

    for combo in win_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# Function to check for a tie
def checkTie():
    return "-" not in board

# Function for the computer's move
def computerMove():
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                        (0, 4, 8), (2, 4, 6)]  # Diagonals

    for combo in win_combinations:
            a, b, c = combo
            if board[a] == board[b] == "O" and board[c] == "-":
                board[c] = "O"
                return
            elif board[a] == board[c] == "O" and board[b] == "-":
                board[b] = "O"
                return
            elif board[c] == board[b] == "O" and board[a] == "-":
                board[a] = "O"
                return

    # Check if the player is about to win, and block the player
    for combo in win_combinations:
        a, b, c = combo
        if board[a] == board[b] == "X" and board[c] == "-":
            board[c] = "O"
            return
        elif board[a] == board[c] == "X" and board[b] == "-":
            board[b] = "O"
            return
        elif board[c] == board[b] == "X" and board[a] == "-":
            board[a] = "O"
            return

    # Try to take the center position (board[4]) if available
    if board[4] == "-":
        board[4] = "O"
        return

    # If none of the above conditions are met, try to take one of the corners
    corners = [0, 2, 6, 8]
    for corner in corners:
        if board[corner] == "-":
            board[corner] = "O"
            return

    # If all else fails, place "O" in an available edge position
    edges = [1, 3, 5, 7]
    for edge in edges:
        if board[edge] == "-":
            board[edge] = "O"
            return

# Main game loop
while True:
    printBoard()
    
    if currentPlayer == "O":
        computerMove()
    else:
        inp = int(input("Enter a number from 1 to 9: "))
        if 1 <= inp <= 9 and board[inp - 1] == "-":
            board[inp - 1] = "X"
        else:
            print("Oops, a player is already in this spot!")

    if checkWin(currentPlayer):
        printBoard()
        print(f"The winner is {currentPlayer}!")
        break
    elif checkTie():
        printBoard()
        print("It's a Tie!")
        break

    currentPlayer = "O" if currentPlayer == "X" else "X"
