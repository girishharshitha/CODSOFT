# Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def calculator():
    print("Simple Calculator")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        operation = input("Enter choice (1/2/3/4/5): ")

        if operation == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif operation == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid operation.")

if __name__ == "__main__":
    calculator()
