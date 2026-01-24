#day 7 
#hangman game 

#randomly choose a word from the word list and assign it to a variable and then print it 
import random 
word_list=["banana","apple","vegetable","camel","baboon"]
chosen_word=random.choice(word_list)

#setting the lives for the game 
lives = 6 

#create a placeholder with the same no of blanks as the choosen word 
placeholder=""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder +="_"
print(placeholder)

#use a while loop to let the user guess again 
game_over = False 
correct_letters =[]
while not game_over:

#ask the user to guess a letter
    guessed_letter=input("Enter the guessed letter\n").lower()

#create a display where the guessed letters are put in the blanks 
#check if the letter the user guessed is right or wrong
#change the for loop to keep the previous letters 

    display=""
    for letter in chosen_word:
        if letter == guessed_letter:
            display += letter 
            correct_letters.append(guessed_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display+= "_"
    print(display)

    #if the guessed letter not in choosen_word
    if guessed_letter not in chosen_word:
        lives -=1
        if lives ==0:
            game_over=True
            print("you lose")
            print(f"it was",{chosen_word})

    if "_" not in display: 
        game_over=True 
        print("you win!congrats...")