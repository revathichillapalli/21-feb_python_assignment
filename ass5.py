

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def calculator():
    print("Welcome to the Python Calculator!")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")
    
    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4/5/6): "))
            
            if choice == 6:
                print("Exiting calculator...")
                break

            if choice not in [1, 2, 3, 4, 5]:
                print("Invalid input! Please choose a valid operation.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == 1:
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 4:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == 5:
                print(f"{num1} raised to the power of {num2} = {power(num1, num2)}")
        
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        
        print("\nChoose another operation or press 6 to exit.\n")

# Run the calculator function
if __name__ == "__main__":
    calculator()
