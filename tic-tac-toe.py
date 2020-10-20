from helpers import getNum

def drawBoard(board):
    print()


def checkWinner(board, player):
    result = False
    if board[0] == board[1] and board[1] == board[2]:
        result = True
    elif board[3] == board [4] and board[4] == board[5]:
        result = True
    elif board[6] == board [7] and board[7] == board[8]:
        result = True
    elif board[0] == board [3] and board[3] == board[6]:
        result = True    
    elif board[1] == board [4] and board[4] == board[7]:
        result = True
    elif board[2] == board [5] and board[5] == board[8]:
        result = True
    elif board[0] == board [4] and board[4] == board[8]:
        result = True
    elif board[2] == board [4] and board[4] == board[6]:
        result = True
    else:
        result = False

    if result == True:
        print ("congratulations!" , player)
    return result
    

def switchPlayer(player):
    if player == "X":
        player = "O"
    else:
        player = "X"

    print ("It's your turn " + player + ".")
    return player
    

def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    currentPlayer = "O"
    gameOver = False
    while not gameOver:
        drawBoard(board)
        currentPlayer = switchPlayer(currentPlayer)
        choice = getNum("Pick a box: ", 1, 9, float("inf"), True)
        while board[choice - 1] == "X" or board[choice - 1] == "O":
            choice = getNum("Enter a number: ", 1, 9, float("inf"), True)
        board[choice - 1] = currentPlayer
        gameOver = checkWinner(board, currentPlayer)

        drawBoard(board):

        player = switchPlayer(currentPlayer)
     
        
        choice = getNum("Pick a box: ", 1, 9, float("inf"), True)
        
      
        while board[choice - 1] == "X" or board[choice - 1] == "O":
            choice = getNum("Enter a number: ", 1, 9, float("inf"), True)

        board[choice - 1] = currentPlayer
        
        gameOver = checkWinner(board, currentPlayer)
        
