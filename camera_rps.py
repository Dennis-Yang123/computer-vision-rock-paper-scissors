# %%
import random
import numpy as np
import cv2
from keras.models import load_model
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


rps = [0, 1, 2] # 0 = rock, 1 = paper, 2 = scissors
rps_string = ["Rock", "Paper", "Scissors"]
def get_computer_choice():
    computer_choice = random.choice(rps)
    return computer_choice


def get_winner(computer_choice, user_choice):
    user_wins = 0
    computer_wins = 0
    if computer_choice == user_choice:
        print("The computer chose", rps_string[computer_choice])
        print("It's a tie!")
   
    elif computer_choice == 0 and user_choice == 2: # rock vs scissors
        print("The computer chose", rps_string[computer_choice])
        print("You lost")
        computer_wins += 1
        
    elif computer_choice == 1 and user_choice == 0: # paper vs rock
        print("The computer chose", rps_string[computer_choice])
        print("You lost")
        computer_wins += 1
        
    elif computer_choice == 2 and user_choice == 1: # scissors vs paper
        print("The computer chose", rps_string[computer_choice])
        print("You lost")
        computer_wins += 1
        
    elif user_choice == 3: # i.e user chooses nothing
        print("Please choose between rock, paper or scissors")
    else: # Only considered computer wins in if statements since anything else is a user win
        print("The computer chose", rps_string[computer_choice])
        print("You won!")
        wins = wins + 1
    return wins
        

def get_prediction():
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
    # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    user_choice = np.argmax(prediction)
    if user_choice == 0:
        print("You chose Rock")
    elif user_choice == 1:
        print("You chose Paper")
    elif user_choice == 2:
        print("You chose Scissors")
    else:
        print("You chose nothing")
    return user_choice

def play(wins):
    print("You have 5 seconds to choose between rock, paper or scissors. Please press q when finsihed.")
    max_time = 9

    start_time = time.time()
    while True:
        if wins < 3:
            while (time.time() - start_time) < max_time:
                get_winner(get_computer_choice(), get_prediction())
        else:
            print("You won three times congratulations!")
            break
        
    
play(0)

# %%
