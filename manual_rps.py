# %%
import random
rps = ["rock", "paper", "scissors"]
def get_computer_choice():
    computer_choice = random.choice(rps)
    print(computer_choice)
    return computer_choice

def get_user_choice():
    user_choice = input("Please choose between rock, paper or scissors")
    user_choice = user_choice.lower()
    if user_choice in rps:
        print(user_choice)
    else:
        print("Please choose between rock, paper or scissors")
    return user_choice
    

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It's a tie!")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("You lost")
    elif computer_choice == "paper" and user_choice == "rock":
        print("You lost")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("You lost")
    else:
        print("You won!")
    

def play():
    get_winner(get_computer_choice(), get_user_choice())

play()

# %%
