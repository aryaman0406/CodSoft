import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_move = random.choice(choices)
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        play_game()

    print("Computer's choice:", computer_move)

    if user_choice == computer_move:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_move == "scissors") or (user_choice == "paper" and computer_move == "rock") or (user_choice == "scissors" and computer_move == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

play_game()

