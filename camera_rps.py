# %%
import random
import numpy as np
import cv2
from keras.models import load_model
import time

model = load_model('keras_model.h5')

rps = [0, 1, 2] # 0 = rock, 1 = paper, 2 = scissors
rps_string = ["Rock", "Paper", "Scissors", "Nothing"]

class RockPaperScissors:
    def __init__(self, model):
        self.model = model
        self.computer_choice = random.choice(rps)
        self.user_wins = 0
        self.computer_wins = 0
        self.count= 5

    def get_computer_choice(self):
        self.computer_choice = random.choice(rps)
        return ()

    def get_winner(self, user_choice):
        if self.computer_choice == user_choice:
            print("The computer chose", rps_string[self.computer_choice])
            print("It's a tie!")
    
        elif self.computer_choice == 0 and user_choice == 2: # rock vs scissors
            print("The computer chose", rps_string[self.computer_choice])
            print("You lost")
            self.computer_wins += 1
            return()
            
        elif self.computer_choice == 1 and user_choice == 0: # paper vs rock
            print("The computer chose", rps_string[self.computer_choice])
            print("You lost")
            self.computer_wins += 1
            return()
            
        elif self.computer_choice == 2 and user_choice == 1: # scissors vs paper
            print("The computer chose", rps_string[self.computer_choice])
            print("You lost")
            self.computer_wins += 1
            return()
            
        elif user_choice == 3: # i.e user chooses nothing
            print("Please choose between rock, paper or scissors")

        else: # Only considered computer wins in if statements since anything else is a user win
            print("The computer chose", rps_string[self.computer_choice])
            print("You won!")
            self.user_wins += 1
            return()
            
    def get_prediction(self):
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        user_victory = "User wins: " + str(self.user_wins)
        pc_victory = "Computer wins: " + str(self.computer_wins)
        # pc_choice = "The Computer chose " + str(rps_string[self.computer_choice])
        time_now = time.time()
        while time.time() < time_now + self.count: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.putText(frame, rps_string[np.argmax(prediction)], (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
            cv2.putText(frame, user_victory, (0, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
            cv2.putText(frame, pc_victory, (0, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
            cv2.putText(frame, str(int((time_now + self.count - time.time()))), (0, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
            # cv2.putText(frame, pc_choice, (0, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

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
            self.get_winner(user_choice)
        elif user_choice == 1:
            print("You chose Paper")
            self.get_winner(user_choice)
        elif user_choice == 2: 
            print("You chose Scissors")
            self.get_winner(user_choice)
        else:
            print("You chose nothing")
        return (user_choice)
        
    def countdown(self):
        cap = cv2.VideoCapture(0)
        time_zero = time.time()
        while time.time() < time_zero + self.count:
            ret, frame = cap.read()
            cv2.putText(frame, "Welcome to Rock Paper Scissors", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
            cv2.putText(frame, "Please choose between the 3", (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def play(model):    
    game = RockPaperScissors(model)
    game.countdown()
    while True:
        if game.user_wins == 3:
            print("Congratulations you have won 3 times")
            restart = input("Press c if you want to restart, or press anything else if you want to quit.")
            if restart.lower() == "c":
                game.computer_wins = 0
                game.user_wins = 0
                game.get_computer_choice()
                game.get_prediction()
            
            else:
                break
            
        elif game.computer_wins == 3:
            print("You lose the computer won 3 times")
            restart = input("Press c if you want to restart, or press anything else if you want to quit.")
            if restart.lower() == "c":
                game.computer_wins = 0
                game.user_wins = 0
                game.get_computer_choice()
                game.get_prediction()
                
            else:
                break             
        else:
            game.get_computer_choice()
            game.get_prediction()
        

if __name__ == "__main__":
    play(model)

# %%
