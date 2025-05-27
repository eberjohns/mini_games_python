from random import randrange

#computer_pick
#player_pick
#is_player_winner

def computer_pick():
    print("\n\nComputer is picking...")
    return randrange(3)

def player_pick():
    while True:
        pick = input("Choose your pick:\n- Rock(r/R)\n- Paper(p/P)\n- Scissor(s/S)\n-> ")
        if pick.lower() == 'r':
            return 0
        elif pick.lower() == 'p':
            return 1
        elif pick.lower() == 's':
            return 2
        else:
            print("Invalid choice. Please choose r, p, or s.")

def is_player_winner(player, computer):
    if player == computer:
        return -1
    elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        return 1
    else:
        return 0

def main():
    print("Welcome to Rock Paper Scissors!")
    while True:
        computer = computer_pick()
        player = player_pick()
        
        choices = ['Rock', 'Paper', 'Scissor']
        print(f"Computer picked: {choices[computer]}")
        
        result = is_player_winner(player, computer)
        if result == 1:
            print(f"\n{choices[player]} beats {choices[computer]} - You Won!")
        elif result == -1:
            print("\nIt's a Tie!")
        else:
            print(f"\n{choices[computer]} beats {choices[player]} - You Lost!")
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y' and play_again != '':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()