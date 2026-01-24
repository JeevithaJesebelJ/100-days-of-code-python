#day 5 
#password generator 

import random

# lists
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')']

print("Welcome to the password generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# ---------------- EASY LEVEL ----------------
easy_password = ""

for _ in range(nr_letters):
    easy_password += random.choice(letters)

for _ in range(nr_symbols):
    easy_password += random.choice(symbols)

for _ in range(nr_numbers):
    easy_password += random.choice(numbers)

print("Your easy password is:", easy_password)

# ---------------- HARD LEVEL ----------------
password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

hard_password = ""
for char in password_list:
    hard_password += char

print("Your hard password is:", hard_password)
