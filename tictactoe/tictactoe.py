from random import randrange

# display_board(board)      to print the board
# victory_for(board)        to check if a player has won
# calculate(board,n,sign)   to update the board with the player's move
# number_available(board,n) to check if a position is available for the move
# computer_move(board)      to draw the computer's move
# person_move(board,sign)   to draw the player's move
# game_round(option)        to initialize the game

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(board[row][0],board[row][1],board[row][2]))
        print("|       |       |       |")
    print("+-------+-------+-------+")

def victory_for(board):
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

def calculate(board,n,sign):
    # The function accepts two parameters: the number of moves made and the sign of the player.
    # It returns the number of moves made by the player.
    n -=1
    board[(int(n/3))][n-((int(n/3))*3)]=sign

    display_board(board)
    
def number_available(board,n):
    # The function checks if the position is available for the move.
    for row in board:
        if n in row: return True
    return False

def computer_move(board):
    # The function draws the computer's move and updates the board.
    found = False
    while not found:
        n = randrange(1,10)
        if number_available(board,n): found = True

    calculate(board,n,'x')

def person_move(board,sign=''):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    found = False
    while not found:
        try:
            n = int(input(f"Enter your move, Person {sign}: " if sign in ['x','o'] else "Enter your move: "))
            if n not in range(1, 10):
                print("!Please enter a number between 1 and 9.")
            elif number_available(board,n): found = True
            else: print("Postion already taken!")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if sign == '':
        calculate(board,n,'o')
    else:
        calculate(board,n,sign)

# The function initializes the game, draws the board, and starts the game loop.
def game_round(option:int):
    if (option==2):
        board=[[1,2,3],[4,5,6],[7,8,9]]
        x=-1
    else:
        board=[[1,2,3],[4,"x",6],[7,8,9]]
        x=0
    display_board(board)
    vic = ''
    while vic=='' and x<8:
        if x%2:
            if(option==2):
                person_move(board,"x")
            else:
                computer_move(board)            
            vic = 'x' if victory_for(board) else ''
        else:
            if(option==2):
                person_move(board,"o")
            else:
                person_move(board)
            vic = 'o' if victory_for(board) else ''
        x +=1

    if (vic==''): print("Draw!") # can also check the condition  if x==8
    elif option==2:
        print("Person "+vic.upper()+" Wins!")
    #below lines are for computer mode that is, when option==1
    elif x%2:
        print("You Won!")
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

if __name__ == "__main__":
    main()
