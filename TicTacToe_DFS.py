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
    available_moves = [i for i in range(9) if board[i] == "-"]
    move = random.choice(available_moves)
    board[move] = "O"

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
