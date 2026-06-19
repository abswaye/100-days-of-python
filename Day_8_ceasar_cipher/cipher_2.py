alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z',]
direction = input("Type 'encode' or 'decode': ")
text = input("Type you're message: ").lower()
shift = int(input("Type your shift number: "))
shift = shift % 26
def caesar(text, shift, direction):
    result = ""

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)

            if direction == "encode":
                new_position = position + shift
            elif direction == "decode":
                new_position = position - shift
            result += alphabet[new_position]
        else:
            result += letter
    print(f"Here is the {direction} result : {result}")
caesar(text, shift, direction)

    

