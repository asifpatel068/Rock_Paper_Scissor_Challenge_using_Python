import random
import sys
# Function to get user's choice
def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        elif choice == "quit":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid choice! Please try again.")

# Function to get computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

# Function to update the score
def update_score(winner, score):
    if winner == "user":
        score["user"] += 1
    elif winner == "computer":
        score["computer"] += 1
    else:
        score["draw"] += 1

# Function to display the score
def display_score(score):
    print(f"User: {score['user']}  Computer: {score['computer']}  Draw: {score['draw']}")

# Main game loop
def play_game():
    score = {"user": 0, "computer": 0, "draw": 0}
    print("Let's play Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"User chooses: {user_choice}")
        print(f"Computer chooses: {computer_choice}")
        winner = get_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win!")
        elif winner == "computer":
            print("Computer wins!")
        else:
            print("It's a draw!")
        update_score(winner, score)
        display_score(score)
        print()
        sys.exit()
# Start the game
play_game()
