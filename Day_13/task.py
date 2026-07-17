# import random
# import maths

# def mutate(a_list):
#     b_list = []
#     new_item = 0

#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#         b_list.append(new_item)

#     print(b_list)

# # mutate([1, 2, 3, 5, 8, 13])
# b_list = []

# for item in [1, 2, 3]:
#     b_list.append(item)

# print(b_list)



# def odd_or_even(number):
#     if number % 2 == 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."

# print(odd_or_even(8))
# def is_leap(year):
#     if year % 4 == 0:          # Question 1
#         if year % 100 == 0:    # Question 2
#             if year % 400 == 0: # Question 3
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# print(is_leap(2000))
# print(is_leap(1900))
# print(is_leap(2024))

# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print((number))
# fizz_buzz(15)
