# Simple Calculator

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Get user input for the operation
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the user input is one of the valid choices
    if choice in ['1', '2', '3', '4']:
        # Get user input for the numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Match the choice to the corresponding operation
        match choice:
            case '1':
                # Perform addition
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            case '2':
                # Perform subtraction
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            case '3':
                # Perform multiplication
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            case '4':
                # Perform division with a check for division by zero
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")

        # Ask the user if they want to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        # Handle invalid input
        print("Invalid input. Please enter a number between 1 and 4.")
