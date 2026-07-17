from calcart import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
num1 = float(input("Whats the first number?:"))
for symbol in operations:
    print(symbol)
operations_symbol = input("Pick your operation: ")
num2 = float(input("Whats the next number?: ")) 
calculation_function = operations[operations_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operations_symbol} {num2} {answer}")
# def format_name(f_name, l_name):
   
#     if f_name == "" or l_name == "":
#         return "You did not provide valid inputs"
#     formatted_f_name = (f_name.title())
#     formatted_l_name = (l_name.title())
#     return f"{formatted_f_name} {formatted_l_name}"
     

# print(format_name(input("What is your first name?"), input("What is your last name?")))
                  


