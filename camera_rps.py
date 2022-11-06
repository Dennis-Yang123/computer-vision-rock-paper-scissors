# %%
import random
from rock_paper_scissors import prediction
import numpy as np
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
    
def get_prediction():
    print(prediction)
    probability = np.argmax(prediction)
    if probability == 0:
        print("You chose rock")
    elif probability == 1:
        print("You've chosen paper")
    elif probability == 2:
        print("You've chosen scissors")
    else:
        print("You chose nothing you are nothing")

def play():
    get_winner(get_computer_choice(), get_user_choice())
    get_prediction()
play()

# %%
