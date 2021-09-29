"""Functions for common math operations."""
# print("Hi")
def calculator():
    input_string = 'pow 3 5'
    tokens = input_string.split(' ')
    while tokens[0] != "q":
            if tokens[0] == "q":
                quit
            elif tokens[0] == "pow":
                return 3**5
            elif tokens[0] == "add or +":
                return 3+5
print(calculator())





#while True:
#input_string = 'pow 3 5'
#tokens = input_string.split(' ')   # => ['pow', '3', '5']
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)

# def add(num1, num2):
#     """Return the sum of the two inputs."""

#     return 10


# def subtract(num1, num2):
#     """Return the second number subtracted from the first."""


# def multiply(num1, num2):
#     """Multiply the two inputs together."""


# def divide(num1, num2):
#     """Divide the first input by the second and return the result."""


# def square(num1):
#     """Return the square of the input."""


# def cube(num1):
#     """Return the cube of the input."""


# def power(num1, num2):
#     """Raise num1 to the power of num2 and return the value."""


# def mod(num1, num2):
#     """Return the remainder of num1 / num2."""
