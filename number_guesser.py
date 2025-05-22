import random

def play_game():
    """Plays a number guessing game with the user."""
    while True:
        difficulty = input("Choose difficulty (type 'easy', 'medium', or 'hard'): ").lower()
        if difficulty == 'easy':
            max_number = 50
            break
        elif difficulty == 'medium':
            max_number = 100
            break
        elif difficulty == 'hard':
            max_number = 500
            break
        else:
            print("Invalid difficulty. Please type 'easy', 'medium', or 'hard'.")

    secret_number = random.randint(1, max_number)
    num_guesses = 0
    while True:
        while True:
            guess_str = input(f"Guess the number (between 1 and {max_number}): ")
            try:
                guess = int(guess_str)
            except ValueError:
                print("Invalid input! Please enter a whole number.")
                continue

            if guess < 1 or guess > max_number:
                print(f"Your guess is out of range! Please enter a number between 1 and {max_number}.")
                continue
            
            # If input is valid and in range, break from this inner loop
            break
        
        num_guesses += 1 # Increment guesses only after a valid guess

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {num_guesses} tries.")
            break

if __name__ == "__main__":
    while True:
        play_game()
        while True:
            play_again_response = input("Do you want to play another round? (yes/no): ").lower()
            if play_again_response == "yes":
                break  # Breaks the inner loop, continues the outer loop to play again
            elif play_again_response == "no":
                print("Thanks for playing!")
                exit()  # Exits the script
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
