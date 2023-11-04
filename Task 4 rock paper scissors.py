
import random

def determine_winner(user_choice, computer_choice):
    # Rock beats scissors, scissors beats paper, paper beats rock
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while True:
        print("Choose: rock, paper, or scissors (or 'quit' to end)")
        user_input = input("Your choice: ").lower()

        if user_input == 'quit':
            break
        if user_input not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")

        result = determine_winner(user_input, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}\n")

    print("Thanks for playing!")

# Play the game
play_game()
