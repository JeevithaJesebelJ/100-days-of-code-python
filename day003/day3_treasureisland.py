#DAY 3 
#TRESSURE ISLAND GAME 

#first hurdle 
print("Welcome to Tressue Island")
print("your mission is to find the tressure")
print("You're at a cross road.Where do you want to go?")
road_direction=input("type 'left' or 'right'")
if road_direction=="left":
    print("You have come to a lake.There is an island in the middle of the lake.")

    #second hurdle 
    transport=input("Type 'wait' to wait for a boat. Type 'swim' to swim across")
    if transport=="wait":
        print("you arrive at the island unharmed. There is a house with 3 doors.")

        #third hurdle 
        color=input("One red,one yellow and one blue.Which color do u choose?")
        if color=="red":
            print("you won the game")
        elif color=="yellow":
            print("Its a room full of fire")
        elif color=="blue":
            print("It's room filled with tigers")
        else:
            print("Enter the correct input")

    #second hurdle 
    elif transport=="swim":
        print("you died while swimming")
    else:
        print("enter correct input")

#first hurdle
elif road_direction=="right":
    print("You reached the wrong path")
else:
    print("enter correct input")


