import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    # Pilih level kesulitan
    choice = input("Enter your choice: ")

    if choice == "1":
        chances = 10
        difficulty = "Easy"
    elif choice == "2":
        chances = 5
        difficulty = "Medium"
    elif choice == "3":
        chances = 3
        difficulty = "Hard"
    else:
        print("Invalid choice! Defaulting to Medium difficulty.")
        chances = 5
        difficulty = "Medium"

    print(f"Great! You have selected the {difficulty} difficulty level.")
    print(f"You have {chances} chances to guess the correct number.")
    print("Let's start the game!")

    # Angka acak
    number_to_guess = random.randint(1, 100)
    attempts = 0

    # Loop permainan
    while chances > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number between 1 and 100.")
            continue

        attempts += 1

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess < number_to_guess:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Incorrect! The number is less than {guess}.")

        chances -= 1

        if chances == 0:
            print(f"Sorry! You've run out of chances. The number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()
