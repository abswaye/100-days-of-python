# from art import logo
# print(logo)
# bids = {}
# keep_bidding = True
# highest_bid = 0
# winner = ""
# while keep_bidding:
#     for bidder in bids:
#         bid_amount = bids[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#         winner = bidder
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
#     if should_continue == "no":
#         keep_bidding = False
# print(f"The winner is {winner} with a bid of ${highest_bid}")





def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)
