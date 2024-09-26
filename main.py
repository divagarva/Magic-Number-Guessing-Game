import random

def magic_number_game():
    print("Welcome to the Magic Number Guessing Game!")
    print("Think of a number between 1 and 100, but don't tell me what it is.")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    guesses = 0

    while True:
        guess = random.randint(low, high)
        guesses += 1
        print(f"Is your number {guess}?")
        feedback = input("Enter 'H' if your number is higher, 'L' if it's lower, or 'C' if it's correct: ").lower()

        if feedback == 'c':
            print(f"Yay! I guessed your number in {guesses} tries. Your number was {guess}!")
            break
        elif feedback == 'h':
            low = guess + 1
        elif feedback == 'l':
            high = guess - 1
        else:
            print("Please enter 'H', 'L', or 'C'.")

if __name__ == "__main__":
    magic_number_game()

