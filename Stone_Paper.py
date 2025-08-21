import random

def game():
    print("Welcome to Stone-Paper-Scissors Game!")
    print("Choices: \n1. Stone \n2. Paper \n3. Scissors")

    choices = ["stone", "paper", "scissors"]

    user_choice = input("Enter your choice (stone/paper/scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please choose stone, paper, or scissors.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You Win!")
    else:
        print("😢 You Lose!")

# Run the game
game()