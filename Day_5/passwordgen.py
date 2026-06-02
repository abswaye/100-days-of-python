import random
print("Welcome to the PyPassword Generator!")
letters_amount = int(input("How many letters would you like?"))

letters = [  "a","b","c","d","e","f","g",
    "h","i","j","k","l","m","n",
    "o","p","q","r","s","t","u",
    "v","w","x","y","z"]

random.shuffle(letters)


numbers_amount = int(input(f"How many numbers would you like?"))
numbers = ["0","1","2","3","4","5","6","7","8","9"]

random.shuffle(numbers)


symbol_amount = int(input("How many symbols would you like?"))
symbols = ["!", "@", "#", "$", "%", "^", "&", "*",
    "(", ")", "-", "_", "+", "=", "{", "}",
    "[", "]", "|", "\\", ":", ";", '"', "'",
    "<", ">", ",", ".", "?", "/"]
random.shuffle(symbols)
password_list = []

password_list += letters[0:letters_amount]
password_list += numbers[0:numbers_amount]
password_list += symbols[0:symbol_amount]

random.shuffle(password_list)

password = "".join(password_list)
print("You random password is:")
print(password)

