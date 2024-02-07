# Define lambda functions for arithmetic operations
addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y if y != 0 else "Error: Division by zero"

# Function to perform arithmetic operations based on user input
def calculate(operation, x, y):
    if operation == '+':
        return addition(x, y)
    elif operation == '-':
        return subtraction(x, y)
    elif operation == '*':
        return multiplication(x, y)
    elif operation == '/':
        return division(x, y)
    else:
        return "Error: Invalid operation"

# Main function
def main():
    print("Welcome to the Simple Calculator!")
    while True:
        # Get user input for operation and numbers
        operation = input("Enter the operation (+, -, *, /) or 'quit' to exit: ")
        if operation == 'quit':
            print("Exiting the calculator. Goodbye!")
            break
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        # Perform calculation and display result
        result = calculate(operation, num1, num2)
        print(f"Result: {result}")

# Run the program
if __name__ == "__main__":
    main()
