from random import randrange

# display_board(board,n,sign) to print the board
# victory_for(board, sign)    to check if a player has won
# computer_move(board)        to draw the computer's move
# person_move(board)          to draw the player's move
# game_round()                to initialize the game

def display_board(board,n=0, sign=''):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    if n!=0:
        n -=1
        board[(int(n/3))][n-((int(n/3))*3)]=sign
    
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(board[row][0],board[row][1],board[row][2]))
        print("|       |       |       |")
    print("+-------+-------+-------+")

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]: return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]: return True
    
    #if   board[0][0] == board[0][1] == board[0][2]: return True
    #elif board[1][0] == board[1][1] == board[1][2]: return True
    #elif board[2][0] == board[2][1] == board[2][2]: return True
    
    #elif board[0][0] == board[1][0] == board[2][0]: return True
    #elif board[0][1] == board[1][1] == board[2][1]: return True
    #elif board[0][2] == board[1][2] == board[2][2]: return True
    
    if   board[0][0] == board[1][1] == board[2][2]: return True
    elif board[2][0] == board[1][1] == board[0][2]: return True
    else: return False


def computer_move(board):
    # The function draws the computer's move and updates the board.
    found = False
    while not found:
        n = randrange(1,10)
        for row in board:
            if n in row: found=True
    display_board(board,n,'x')

def person_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    found = False
    while not found:
        n = int(input("Enter your move: "))
        for row in board:
            if n in row: found=True
    display_board(board,n,'o')

# The function initializes the game, draws the board, and starts the game loop.
def game_round():
    board=[[1,2,3],[4,"x",6],[7,8,9]]
    display_board(board)
    x=0
    vic = False
    while not vic and x<8:
        if x%2:
            computer_move(board)
            vic = victory_for(board,"x")
        else:
            person_move(board)
            vic = victory_for(board,"o")
        x +=1

    if x==8: print("Draw!")
    elif x%2: print("You Won!")
    else: print("I Won!")

def main():
    print("Welcome to Tic Tac Toe!")
    want_to_play = "y"
    while want_to_play == "y":
        game_round()
        want_to_play = input("Do you want to play again? (y/n): ").lower()
    print("Thanks for playing!")

main()