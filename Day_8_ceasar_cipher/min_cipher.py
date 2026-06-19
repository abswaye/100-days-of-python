# # fruits = ["apple", "banana", "cherry"]
# # print(fruits)
# numbers = [1, 2, 3, 4, 5]
# doubled = []
# for number in numbers:
#     doubled.append(number * 2)
# print(doubled)
# numbers = [1, 2, 3, 4]
# new_numbers = []
# for number in numbers:
#     new_numbers.append(number + 10)
# # print(new_numbers)
#practice1 first try 
# numbers = [2, 4, 6, 8]
# doubled_numbers = []
# for number in numbers:
#     doubled_numbers.append(number * 2)
# print(doubled_numbers)
# #Practice 2
# names = ["alex", "sam", "jordan"]
# loud_names = []
# for name in names:
#     loud_names.append(name.upper())
# # print(loud_names)
# #Practice 3
# prices = [5, 10, 15]
# discount_prices = []
# for price in prices:
#     discount_prices.append(price - 2)
# print(discount_prices)
# letters = ["c", "a", "t"]
# word = ""
# for letter in letters:
#     word += letter
# print(word)
# letters = ["p", "y", "t", "h", "o", "n"]
# word = []
# for letter in letters:
#     word += letter
# # print(word)
# words = ["I" ,  "like" ,  "code"]
# sentence = ""
# for word in words:
# #     sentence += word + " "
# # print(sentence)
# letters = ["a", "b", "c"]
# result = ""
# for letter in letters:
# #     result += letter + "-"
# # print(result)
# words = ["go", "team", "python"]
# result = ""
# for word in words:
#     result += word + "!"
# # print(result)
# names = ["alex", "jordan", "sam"]
# initials = ""
# for name in names:
#     initials += name[0]
# # print(initials)
# letters = ["a", "b", "c"]
# alphabet = ["a", "b", "c", "d", "e"]
# result = ""
# for letter in letters:
#     position = alphabet.index(letter)
#     new_position = position + 1
#     new_letter = alphabet[new_position]
#     result += new_letter
# print(result)

# message_letters = ["a", "b", "c"]
# alphabet = ["a", "b", "c", "d", "e"]
# result = ""
# for letter in message_letters:
#     position = alphabet.index(letter)
#     new_position = position + 1
#     new_letter = alphabet[new_position]
#     result += new_letter
# # print(result)

# numbers = [1, 2, 3]
# result = []
# for number in numbers:
#     result.append(number + 10)
# print(result)
message_letters = ["a", "b", "c"]
alphabet = ["a", "b", "c", "d", "e"]
result = ""
for letter in message_letters:
    position = alphabet.index(letter)
    new_position = position + 1
    new_letter = alphabet[new_position]
    result += new_letter
print(result)
