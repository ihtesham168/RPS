import random


def get_computer_choice(): 
    return random.choice(["Rock" , "Paper", "Scissors"])
    

def get_user_choice():

    user_selection= input(' Please enter your choice please  ')
    return user_selection



def get_winner(comp_selection , user_selection):

    if user_selection==comp_selection:

        print(f"Its a Tie! You and Computer makes same choice")



    elif user_selection=="Rock" and comp_selection == "Paper":
        print(f"Oops! You Lose Computer selected{ comp_selection}")
            




    elif user_selection == "Rock" and comp_selection == 'Scissors':
        print(f"Congrats! You Win. Computer selected { comp_selection}")
        


    elif user_selection == "Paper" and comp_selection =="Scissors":
        print(f"Oops! You Lose, Computer selected { comp_selection}")
        



    elif user_selection == "Paper" and comp_selection == "Rock":
        print(f"Congrats! You Win. Computers selected { comp_selection}")
       
   
   
   
    elif user_selection == "Scissors" and comp_selection == "Rock":
        print(f"Oops! You Lose. Computer slected { comp_selection}")
        
    
   
   
    elif   user_selection == "Scissors" and comp_selection == "Paper":
            print(f"Congrats! You Win. Computer selected { comp_selection}")
        


def play():
    
    user= get_user_choice()
    computer= get_computer_choice()
    get_winner(computer,user )
    
    
    
 
play()
 
   

