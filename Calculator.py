def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("=== Simple Calculator ===")
    print("\n")
    print("Operations: +, -, *, /")

    while True:
        try:
            a = float(input("\nEnter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            b = float(input("Enter second number: "))

            if op == "+":
                print(f"Result: {add(a, b)}")
            elif op == "-":
                print(f"Result: {subtract(a, b)}")
            elif op == "*":
                print(f"Result: {multiply(a, b)}")
            elif op == "/":
                print(f"Result: {divide(a, b)}")
            else:
                print("Invalid operator. Try again.")

        except ValueError:
            print("Please enter valid numbers.")

        again = input("\nCalculate again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break

calculator()