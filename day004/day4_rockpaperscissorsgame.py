#day4 
#project : Rock paper scissors game 

import random 
print("welcome to the game")
user_input=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors"))

#defining computer inputs
comp_input= random.randint(0,2)
if comp_input==0:
    print("computer chose rock")
elif comp_input==1:
    print("computer chose paper")
elif comp_input==2:
    print("computer chose scissors")

#game logic 
if comp_input==user_input:
    print("It is a tie!")
elif (comp_input ==0 and user_input==1):
    print("u won!congrats...")
elif(comp_input==0 and user_input==2):
    print("computer won!")
elif(comp_input==1 and user_input==0):
    print("computer won!")
elif(comp_input==1 and user_input==2):
    print("u won!congrats...")
elif(comp_input==2 and user_input==0):
    print("u won!congrats...")
elif(comp_input==2 and user_input==1):
    print("computer won!")



