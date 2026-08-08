def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def power(a, b):
    return a ** b


def calculator():
    history = []

    while True:
        print("\n===== CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. View History")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Thank you for using the calculator!")
            break

        if choice == "6":
            if history:
                print("\nCalculation History:")
                for calculation in history:
                    print(calculation)
            else:
                print("No calculations yet.")
            continue

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(num1, num2)
            operator = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"

        elif choice == "4":
            result = divide(num1, num2)
            operator = "/"

            if result is None:
                print("Error: Cannot divide by zero.")
                continue

        elif choice == "5":
            result = power(num1, num2)
            operator = "**"

        calculation = f"{num1} {operator} {num2} = {result}"
        history.append(calculation)

        print("Result:", result)


calculator()
