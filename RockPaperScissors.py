import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    user_choice = input("Enter Rock, Paper, or Scissors (or Q to quit): ").capitalize()
    
    if user_choice == "Q":
        break
    
    if user_choice not in choices:
        print("Invalid input. Please try again.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer choice: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("You lose!")
