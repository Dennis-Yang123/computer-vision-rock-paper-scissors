# %%
import random
from rock_paper_scissors import prediction
import numpy as np
rps = [0, 1, 2] # 0 = rock, 1 = paper, 2 = scissors
def get_computer_choice():
    computer_choice = random.choice(rps)
    print(computer_choice)
    return computer_choice

# def get_user_choice():
    # user_choice = input("Please choose between rock, paper or scissors")
    # user_choice = user_choice.lower()
    # if user_choice in rps:
        #print(user_choice)
    # else:
        #print("Please choose between rock, paper or scissors")
    # return user_choice
    

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It's a tie!")
    elif computer_choice == 0 and user_choice == 2: # rock vs scissors
        print("You lost")
    elif computer_choice == 1 and user_choice == 0: # paper vs rock
        print("You lost")
    elif computer_choice == 2 and user_choice == 1: # scissors vs paper
        print("You lost")
    else:
        print("You won!")
    
def get_prediction():
    print(prediction)
    user_choice = np.argmax(prediction)
    if user_choice == 0:
        print("You chose rock")
    elif user_choice == 1:
        print("You've chosen paper")
    elif user_choice == 2:
        print("You've chosen scissors")
    else:
        print("You chose nothing you are nothing")
    return user_choice

def play():
    get_winner(get_computer_choice(), get_prediction())

play()

# %%
