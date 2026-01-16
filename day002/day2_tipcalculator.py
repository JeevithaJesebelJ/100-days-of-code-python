#day2
#tip calculator 

#bill amount 
print("Welcome to the tip calculator!")
bill_amount=float(input("what was the total bill?"))

#tip amount 
tip_percentage=int(input("How much tip would you like to give? 10,12 or 15?"))
if tip_percentage == 10:
    tip_amount = 0.1 * bill_amount
elif tip_percentage ==12:
    tip_amount = 0.12 *bill_amount
elif tip_percentage ==15:
    tip_amount= 0.15*bill_amount 
else:
    print("tip amount is not defined")

#total bill= bill amount +tip amount 
total_bill= bill_amount+tip_amount

#each person's share 
no_of_people=int(input("How many people to split the bill?"))
individual_amount= total_bill/no_of_people
individual_amount=round(individual_amount,2)
print(f"Each person should pay: $ {individual_amount}")