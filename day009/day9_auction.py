#secret auction program 

print("Welcome to the auction")

bidding_dictionary = {}

def bidding_function():
    bidder_name = input("Enter your name: \n")
    bidder_price = int(input("Enter the price you are ready to offer: $\n"))

    bidding_dictionary[bidder_name] = bidder_price

    more_bid = input("Are there any more bids? Type 'yes' or 'no': \n")

    if more_bid == "yes":
        print("\n"*100)
        bidding_function()
    else:
        print("\n"*100)
        highest_bid = 0
        winner = ""

        for bidder in bidding_dictionary:
            price = bidding_dictionary[bidder]

            if price > highest_bid:
                highest_bid = price
                winner = bidder

        print(winner, "is the highest bidder with $", highest_bid)

bidding_function()
