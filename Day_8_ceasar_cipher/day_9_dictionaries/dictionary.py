# bids = {}
# keep_bidding = True
# while keep_bidding:

#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
#     if should_continue == "no":
#         keep_bidding = False

# print(bids)            
# ages = {
#     "Mia": 12,
#     "Jordan": 17,
#     "Alex": 25,
#     "Sam": 70
# }

# age_groups = {}
# for name in ages:
#     age = ages[name]
#     if age >= 65:
#         age = "Senior"
#     elif age >= 18:
#         age = "Adult"
#     elif age >= 13:
#         age = "Teen"
#     else:
#         age = "Child"
#     age_groups[name] = age
# print(age_groups)

stock = {
    "apples": 30,
    "bananas": 0,
    "oranges": 8,
    "grapes": 15
}

status = {}
for item in stock:
    amount = stock[item]
    if amount>= 20:
        label = "Plenty"
    elif amount>= 1:
        label = "Low"
    else:
        label = "Out of stock"
    status[item] = label
print(status)
