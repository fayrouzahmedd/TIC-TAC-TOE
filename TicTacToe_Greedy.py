import random
board = ["-", "-", "-", 
        "-", "-", "-", 
        "-", "-", "-", ]

currentPlayer = "O"
winner = None
gameRunnning = True

# Game Board
def printBoard(board):
    print("")
    print(f"                             " + board[0] + " | " + board[1] + " | " + board[2])
    print("                             ---------")
    print(f"                             " + board[3] + " | " + board[4] + " | " + board[5])
    print("                             ---------")
    print(f"                             " + board[6] + " | " + board[7] + " | " + board[8])
    print("")

# Take player input
def playerInput(board):
    inp = int(input("Enter a number from 1 to 9: "))
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already in this spot!")

# Check for win Horizontally
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and  board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and  board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and  board[7] != "-":
        winner = board[6]
        return True

# Check for win Vertically
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and  board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and  board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and  board[2] != "-":
        winner = board[2]
        return True

# Check for win Diagonally
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and  board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and  board[2] != "-":
        winner = board[2]
        return True

# Check if Tie
def checkTie(board):
    global gameRunnning
    if "-" not in board:
        printBoard(board)
        print("It is a Tie!")
        gameRunnning = False

# Check Winner
def checkWin():
    global gameRunnning
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        print(f"==========================The winner is {winner}===========================")

# Switching Players
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Computer Greedy
def computer(board):
    if currentPlayer == "O":
        best_move = None
        best_score = -1  # Initialize to a value lower than any possible score

        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                if checkWin():
                    best_move = i
                    board[i] = "O"  # Make the winning move
                    return
                board[i] = "-"

                # Count the number of adjacent O's for the current move
                score = 0
                for j in range(9):
                    if board[j] == "O":
                        score += 1

                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move is not None:
            board[best_move] = "O"
            switchPlayer()


while gameRunnning:
    computer(board)
    printBoard(board)
    playerInput(board)
    switchPlayer()
    checkWin()
    checkTie(board)
    computer(board)