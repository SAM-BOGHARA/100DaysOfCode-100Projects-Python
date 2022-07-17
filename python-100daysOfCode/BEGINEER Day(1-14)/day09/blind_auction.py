from art import logo


print(logo)

dict = {}


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        amount = bidding_record[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The Winner is {winner} with bid of ${highest_bid}")


bidders_remaining = True
while bidders_remaining:
    name = input("What is bidder's name :>  ")
    bid_price = int(input("What is your bid :>  $"))

    dict[name] = bid_price
    choice = input(
        "Is there any other bidder,type 'yes' to continue or else type 'no' :>  ").lower()
    # print(dict)
    if choice == "no":
        bidders_remaining = False
        highest_bidder(dict)
    else:
        print("\n" * 100)
