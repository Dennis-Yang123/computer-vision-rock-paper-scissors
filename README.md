# Computer Vision Project
## Milestone 2
### Task 1 & 2
For this task I was asked to create an image project model on Teachable-Machine showing images of me holding up a Rock/Paper/Scissors or nothing to train the model. I then downloaded it and pushed it to Github.

## Milestone 3
For this milestone I was tasked to create a `conda` environment and install `opencv-python`, `ipykernel` and `tensorflow` and their dependencies.

## Milestone 4
For this milestone I was tasked to create a Python script that would simulate a Rock-Paper-Scissors game. 

This was pretty straightforward task which included use of functions and if/else statements.

## Milestone 5
For this milestone I was asked to create the Rock Paper Scissors game using the model made previously on Teachable-Machine and putting it all together.

### Task 1
For this task I was asked to create a new file `camera_rps.py` to write the new code and to create a new function `get_prediction()` where it woudl return the output of the model.

### Task 2
For this task I was asked to create a countdown to the player showing their hand without using the `time.sleep` function as it would freeze the code. To solve this I used the `time.time()` function.

I created a `countdown()` method in the RockPaperScissors class and using a while loop: 
```
time_zero = time.time()
while time.time() < time_zero + self.count:
```
The code above would run every 5 seconds where `count` is an attribute set to 5. This `countdown()` method would be the introduction to the game and using `opencv` I used the `VideoCapture` and `putText` functions to load the camera and overlay the countdown and other text onto the frame. I have also done this for the `get_prediction()` method to countdown when the code would take the image and make its prediction.

### Task 3
For this task I was asked to repeat the game until the player or the computer reach three victories. To do this I wrote the if-statements and code for the win conditions in the `play(model)` function which is a separate function that plays the game. 
```
while True:
        if game.user_wins == 3:
            print("Congratulations you have won 3 times")
            restart = input("Press c if you want to restart")
            if restart.lower() == "c":
                game.computer_wins = 0
                game.user_wins = 0
                game.get_computer_choice()
                game.get_prediction()
            
            else:
                break
            
        elif game.computer_wins == 3:
            print("You lose the computer won 3 times")
            restart = input("Press c if you want to restart")
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
```
From the code above you can see that I created a While loop and if-statements where if the user wins 3 times it would congratulate the user and otherwise if the computer won 3 times it would tell the user they lost amongst other things which will be discussed later.

### Task 4 (Optional)
For this optional task I was asked to find ways to improve the application and user experience. Some of the suggested ways included printing a countdown in the webcam display or including a message like "press c to continue". 

For the second part we can refer to the code above in the `play(model)` function. In the if-statements for both the user wins and computer wins I created a variable `restart` which asks the user to type in c to restart the game which then if the user presses c it resets the number of user and computer wins to 0 and starts up the game again. If the user chooses to not play it breaks the while loop and the program is ended. A copy of this process is done in the case for the computer winning 3 times.

For the first part we can look at the code below:
```
cv2.putText(frame, str(int((time_now + self.count - time.time()))), (0, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
```
Using the `putText` function I can directly overlay text onto the webcam and using the line `str(int((time_now + self.count - time.time())))` turns the time into an integer and then to a string for it to display the countdown.

Thank you for reading this commentary.