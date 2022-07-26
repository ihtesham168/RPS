#Importing necessary libraries
import cv2
from keras.models  import load_model
import numpy as np
import random
import time

#Rock, Paper, Scissors, class
class Rps:
    
    def __init__(self):
        self.model = load_model("keras_model.h5")

        self.computer_score = 0
        self.user_score = 0
        
    def get_computer_choice(self):

        return random.choice(["rock" , "paper", "scissors"])

    def get_prediction(self):

        cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            cv2.imshow("frame", frame)

            prediction = self.model.predict(self.data)
            max_index = np.argmax(prediction[0])
            print(max_index)
        return max_index

    def get_user_choice(self):
        max_index = self.get_prediction()
        print(max_index)

       
    def get_winner(self,user_selection, comp_selection ):

        if user_selection== comp_selection():
            print(f"Its a Tie! You and Computer makes same choice")

        elif user_selection == "Rock" and comp_selection == "Paper":
            print(f"Oops! You Lose Computer selected{ comp_selection}")
            self.computer_score += 1    

        elif user_selection == "Rock" and comp_selection == 'Scissors':
            print(f"Congrats! You Win. Computer selected { comp_selection}")
            self.user_score += 1

        elif user_selection == "Paper" and comp_selection =="Scissors":
            print(f"Oops! You Lose, Computer selected { comp_selection}")
            self.computer_score += 1

        elif user_selection == "Paper" and comp_selection == "Rock":
            print(f"Congrats! You Win. Computers selected { comp_selection}")
            self.user_score += 1
   
        elif user_selection == "Scissors" and comp_selection == "Rock":
            print(f"Oops! You Lose. Computer slected { comp_selection}")
            self.computer_score += 1
    
        elif   user_selection == "Scissors" and comp_selection == "Paper":
            print(f"Congrats! You Win. Computer selected { comp_selection}")
            self.user_score += 1
        

        def play(self):
             while self.computer_score <3 and self.user_score <3:
                comp_selection = game.get_comp_selection()
                
            


                print(f"Computer choice : {comp_selection}   User choice : {user_selection}")
                print (game.get_winner(comp_selection,user_selection))
                print (f"Scores : Computer - {self.computer_score}    User - {self.user_score}")

game = Rps()
game.get_user_choice()


    