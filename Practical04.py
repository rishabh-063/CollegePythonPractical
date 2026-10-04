# Handle ValueError, ZeroDivisionError and other runtime errors.

try: 
    a = int(input("Numerator: "))
    b = int(input("Denominator: "))
    print("Result: ",a/b)
except ValueError :
    print("Enter integer only")  
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution completed")

# Create, raise and handle a custom exception

class AgeError(Exception):
    pass
try:
    age = int(input("Enter age:"))
    if age<18:
        raise AgeError("Age must be 18 or above")
    print("Eligible")
except AgeError as e:
    print("Custom Exception:",e)