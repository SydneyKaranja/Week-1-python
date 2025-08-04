def main():
    # Print a welcome message
    print("Simple Calculator")
    
    # Ask the user to enter the first number and convert it to float
    num1 = float(input("Enter the first number: "))
    
    # Ask the user to enter the second number and convert it to float
    num2 = float(input("Enter the second number: "))
    
    # Ask the user to enter the operation (+, -, *, /)
    operation = input("Enter operation (+, -, *, /): ")

    # Perform addition if user entered '+'
    if operation == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    # Perform subtraction if user entered '-'
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    # Perform multiplication if user entered '*'
    elif operation == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    # Perform division if user entered '/'
    elif operation == '/':
        # Check for division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    # Handle invalid operation input
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")

# Ensure the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()