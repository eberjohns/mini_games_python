from random import randrange

# display_board(board,n,sign) to print the board
# victory_for(board, sign)    to check if a player has won
# computer_move(board)        to draw the computer's move
# person_move(board,sign)          to draw the player's move
# game_round(option)                to initialize the game

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

def person_move(board, sign='c'):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    found = False
    while not found:
        if sign=='c':
            n = int(input("Enter your move: "))
        else:
            n = int(input("Enter your move, Person "+sign+": "))
        for row in board:
            if n in row: found=True
    if sign=='c':
        display_board(board,n,'o')
    else:
        display_board(board,n,sign)

# The function initializes the game, draws the board, and starts the game loop.
def game_round(option:int):
    if (option-1):
        board=[[1,2,3],[4,5,6],[7,8,9]]
        x=-1
    else:
        board=[[1,2,3],[4,"x",6],[7,8,9]]
        x=0
    display_board(board)
    vic = False
    while not vic and x<8:
        if x%2:
            if(option-1):
                person_move(board,"x")
            else:
                computer_move(board)            
            vic = victory_for(board,"x")
        else:
            if(option-1):
                person_move(board,"o")
            else:
                person_move(board)
            vic = victory_for(board,"o")
        x +=1

    if x==8: print("Draw!")
    elif x%2: 
        if (option-1):
            print("Person O Wins!")
        else:
            print("You Won!")
    else:
        if (option-1):
            print("Person X Wins!")
        else:
            print("I Won!")

def main():
    print("Welcome to Tic Tac Toe!")
    want_to_play = "y"
    while want_to_play == "y":
        option = 0
        while not option:
            try:
                option = int(input(
                    "Choose your opponent: \n" \
                    "1. Computer\n" \
                    "2. Player V/S Player\n" \
                    "---> " \
                    ))
                if option not in [1, 2]:
                    print("Invalid choice. Please choose 1 or 2.")
                    option = 0
            except ValueError:
                print("Invalid input. Please enter a number.")
        game_round(option)
        want_to_play = input("Do you want to play again? (y/n): ").lower()
    print("Thanks for playing!")

main()