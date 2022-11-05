# %%
import random
rps = ["rock", "paper", "scissors"]
def get_computer_choice():
    comp_choice = random.choice(rps)
    print(comp_choice)

def get_user_choice():
    user_choice = input("Please choose between rock, paper or scissors")
    user_choice = user_choice.lower()
    if user_choice in rps:
        print(user_choice)
    else:
        print("Please choose between rock, paper or scissors")

