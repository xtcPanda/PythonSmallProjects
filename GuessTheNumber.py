import random

print("Welcome to the Guess the Number game!")
lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))
secret_number = random.randint(lower_bound, upper_bound)
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    guess = int(input(f"Guess the secret number ({lower_bound} - {upper_bound}): "))
    attempts += 1
    if guess == secret_number:
        print(f"Congratulations! You guessed the secret number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

if attempts == max_attempts:
    print(f"Sorry, you have reached the maximum number of attempts ({max_attempts}). The secret number was {secret_number}.")
