import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in choices:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'scissors' and computer == 'paper') or
        (user == 'paper' and computer == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    result = determine_winner(user, computer)
    print(result)

if __name__ == "__main__":
    play()