import random

def hangman(word):
    wrong_guesses = 0
    stages = ["",
              "_________        ",
              "|                ",
              "|        |       ",
              "|        0       ",
              "|       /|\      ",
              "|       / \      ",
              "|                ",
             ]
    remaining_letters = list(word)
    letter_board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    
    while wrong_guesses < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter: ")
        
        if guess in remaining_letters:
            index = remaining_letters.index(guess)
            letter_board[index] = guess
            remaining_letters[index] = "$"
            
        else:
            wrong_guesses += 1
            
        print(" ".join(letter_board))
        e = wrong_guesses + 1
        print("\n".join(stages[0: e]))
        
        if "_" not in letter_board:
            print("Congratulations! You win!")
            print(" ".join(letter_board))
            win = True
            break
            
    if not win:
        print("\n".join(stages[0:wrong_guesses]))
        print("Sorry, you lose. The word was {}.".format(word))

words_list = ["cat", "dog", "bird", "elephant", "giraffe", "monkey", "snake"]
random_index = random.randint(0, len(words_list)-1)
word = words_list[random_index]
hangman(word)
