"""Practical 1: Operators, data types, strings, conditionals, and loops."""

# Operators
first_number = 17
second_number = 5
print("\nOperators --")
print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)
print("Floor division:", first_number // second_number)
print("Remainder:", first_number % second_number)
print("Power:", first_number**2)
print("17 is greater than 5:", first_number > second_number)


# Built-in data types
print("\nData Types --")
values =  ["Python",10,3.14,True]
for value in values:
    print(value, "->", type(value).__name__)

# String operations
print("\nStrings --")
message = "Python Programming"
print("Original:", message)
print("First character:", message[0])
print("First six characters:", message[:6])
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Length:", len(message))
print("Replace:", message.replace("Programming", "Basics"))

# Conditional statements
print("\nConditional Statements --")
number = int(input("Enter an integer: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Looping statements
print("\nFor Loop: Multiplication Table --")
for multiplier in range(1, 11):
    print(f"{number} x {multiplier} = {number * multiplier}")

