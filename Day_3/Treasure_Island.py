print('''      
        \ _ /
      -= (_) =-
        /   \         _\/_
          |           //o\  _\/_
   _____ _ __ __ ____ _ | __/o\\ _
 =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
  =- _=-=- -_=-=_,-"          |
jgs =- =- -=.--"
''')
print("Welcome to Treasure Island. ")
print("You're mission is to find the treasure")

choice1 = input("Do you want to go Left or Right? ").lower()

if choice1 == "left":

    choice2 = input("swim or wait? ").lower()
    if choice2 == "wait":
      choice3 = input("Which door? red, blue o yellow? ").lower()
    else:
        print("You fell into a hole. Game over!")

     
       
      
    if choice3 == "red":
          print("Burned by fire. Game over!")
    elif choice3 == "blue":
          print("Eaten by beasts. Game Over!")
    elif choice3 == "Yellow":
         print("You won!")
    else:
         print("Game Over!")
else:
   
  print("Fall into a hole. Game over!")



