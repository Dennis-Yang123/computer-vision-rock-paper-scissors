# %%
import random
from rock_paper_scissors import prediction
import numpy as np
import cv2
from keras.models import load_model
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

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
    elif user_choice == 3: # i.e user chooses nothing
        print("Please choose between rock, paper or scissors")
    else:
        print("You won!")

    
    
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
        print("You chose rock")
    elif user_choice == 1:
        print("You've chosen paper")
    elif user_choice == 2:
        print("You've chosen scissors")
    else:
        print("You chose nothing")
    return user_choice

def play():
    print("Please choose between rock, paper or scissors when the countdown is complete then press q when finished")
    
    get_winner(get_computer_choice(), get_prediction())
    
play()

# %%
