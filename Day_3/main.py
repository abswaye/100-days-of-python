# #In this lesson we learn conditionals
print("Welcome to the roller coaster")
height_to_check = int(input("What is your height in cm?"))
bill = 0
if height_to_check >= 120:
     print("You are tall enough to ride.")
     age = int(input("What is your age?"))
     if age <= 12:
         print("Please pay $5")
         bill = 5
     elif age <= 18:
        print("Please pay $7.")
        bill = 7
     else:
        print("Please pay $12.")
        bill = 12
     photos = input("Do you want photos?")
     if photos == "yes":
         print("please pay $3.")
         bill += 3 
print(f"Your final bill is {bill}")
