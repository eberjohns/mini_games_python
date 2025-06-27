from random import randrange

# Function to pick a random number between 0 and n-1
def pick_number(limit):
    return randrange(limit)

# Function to get the player's guess
def get_player_guess(limit):
    while True:
        try:
            guess = int(input(f"Guess a number between 0 and {limit - 1}: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function to run the game
def main():
    print("Welcome to Guess The Number!")

    z = 1
    while z == 1:
        attempts = 0  # To count number of attempts

        # Get the upper limit from the user
        while True:
            try:
                limit = int(input("Enter the upper limit for the guessing range: "))
                if limit < 2:
                    print("Please enter a number greater than 1.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Random number to be guessed
        secret_number = pick_number(limit)

        # Loop until the player guesses the correct number
        while True:
            player_guess = get_player_guess(limit)
            attempts += 1

            if player_guess < secret_number:
                print("Too low! Try again.")
            elif player_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            
        # Ask if they want to continue
        try:
            z = int(input("Do you want to continue? (1 = Yes, 0 = No): "))
        except ValueError:
            print("Invalid input. Exiting game.")
            break

# Run the main function
if __name__ == "__main__":
    main()
