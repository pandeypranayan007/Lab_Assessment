# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Main program loop
while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Taking user choice
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break  # Exit the loop

    # Taking user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Performing calculations based on user choice
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} × {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} ÷ {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input! Please enter a valid choice.")
1