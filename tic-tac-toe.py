from helpers import getNum

def drawBoard(board):
    #TODO - Print the values in the board array parameter. Format them in a tic-tac-toe board (Keegan)
    # 1 | 2 | 3
    #-----------
    # 4 | 5 | 6
    #-----------
    # 7 | 8 | 9

def checkWinner(board, player):
    # TODO - Write an if statement to check if there are 3 matching values. Note: there are 8 different combinations to win. For example, if board indexes 0, 1, and 2 are all equal we have a winner. You will need to combine 8 boolean expressions with "or" operators. (Joss)
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
        return = False

    if result == True:
        print ("congratulations!" , currentPlayer)
    return result


        # TODO - If true, print a message to congratulate the player that won and return True (Danielle)
        
    # TODO - Otherwise, return False (Danielle)
    

def switchPlayer(player):
    # TODO - Write an if-else statement to change the player from "X" to "O", and vice versa. (Danielle)
    if player == "X":
        player = "O"

    else:
        player = "X"

    # TODO - Print a message indicating who the current player is. And return the player variable. (Jason)
    print ("It's your turn " + player + ".")
    return player
    

def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    currentPlayer = "O"
    gameOver = False
    # TODO - Write  while a loop that will run continuosly while the game is not over. Use the gameOver variable. (Jason)
    
    while not gameOver:
        
        # TODO - Call the drawBoard function, passing the board array to the function. No value will be returned. (Tresha)
        
        # TODO - Call the switchPlayer function, passing the currentPlayer variable as the argument. The result returned will be assigned back to the currentPlayer variable. (Tresha)
        
        # TODO - Prompt the player for a number between 1 and 9. Give them an infinite amount of attempts. Convert the numerical input to an integer. Assign the player's response to the choice variable. (Emma)
        choice = getNum("Pick a box: ", 1, 9, float("inf"), True)
        
        # TODO - Using the choice variable, write a while loop that checks if an "X" or "O" is currently located at the index the player chose. Note: if the user chooses 1, we need to check the value at index 0. If true, prompt the user for another choice using the same logic as the previous TODO (Paula)
        

        # TODO - Assign the currentPlayer variable to location the player chose in the board array. Note: if the user chooses 1, we need to assign the value to index 0. (Jeremy)
        board[choice - 1] = currentPlayer
        
        # TODO - Call the checkWinner function. Pass the board array and the currentPlayer to the function. The value returned will be assigned to the gameOver variable. (Jeremy)
        gameOver = checkWinner(board, currentPlayer)
        



main()