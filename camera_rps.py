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
        choice = ['Rock','Paper','Scissors']
        comp_choice = random.choice(choice)
        return comp_choice

    def get_prediction(self):

        self.cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        current = time.time()

        while current+5 > time.time(): 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, str(int(current-time.time()+5)),
                        (200, 250), font,
                        7, (0, 255, 255),
                        4, cv2.LINE_AA)

           
            cv2.imshow("frame", frame)

            if cv2.waitKey(1) == ord('q'):
                break


        prediction = self.model.predict(data)
        max_index = np.argmax(prediction[0])
        return max_index
   
    def get_user_choice(self):
        max_index = self.get_prediction()
        if max_index == 0:
            user_choice = "Rock"
        elif max_index == 1:
            user_choice = "Paper"
        elif max_index == 2:
            user_choice = "Scissors"
        else:
            user_choice = "Nothing"

        return user_choice
   
    def get_winner(self):

        user_selection = self.get_user_choice()
        comp_selection = self.get_computer_choice()
        print(user_selection)
        print(comp_selection)
        if user_selection == comp_selection:
            print(f"Its a Tie! You and Computer makes same choice")

        elif comp_selection == 'Rock' and user_selection =='Paper':
            self.user_score+= 1
            print("User Won")
       
        elif comp_selection == 'Paper' and user_selection == 'Scissors':
            self.user_score += 1
            print("User Won")
            #return "User won"

       
        elif comp_selection == 'Scissors' and user_selection == 'Rock':
            self.user_score += 1
            print("User Won")
            #return "User won"

        
        else:
            self.computer_score += 1
            return "Computer won"
        
        
    def play(self):
        while self.computer_score <3 and self.user_score <3:
        
            self.get_winner()        
           # print(f"Computer choice : {comp_selection}   User choice : {user_selection}")
            #print (game.get_winner())
            print (f"Scores : Computer - {self.computer_score}    User - {self.user_score}")

        self.cap.release()

        cv2.destroyAllWindows()

game = Rps()
game.play()



    
