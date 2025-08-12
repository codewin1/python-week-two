#Here is a basic calculator that prompts the user for inputs then perfoms the required operation.
#I have decided to use a function to encapsulate the  logic.
def basic_calculator():
    # Get inputs from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

    # Perform the operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            return  # this is to handle division by zero
    else:
        print("Invalid operation.")
        return  

    # Print the result
    print(f"{num1} {operation} {num2} = {result}")

# Call the function to run the calculator
basic_calculator()

