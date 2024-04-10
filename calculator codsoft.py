def calculator():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        result = a + b
        print("The result of addition is:", result)
    elif choice == 2:
        result = a - b
        print("The result of subtraction is:", result)
    elif choice == 3:
        result = a * b
        print("The result of multiplication is:", result)
    elif choice == 4:
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = a / b
            print("The result of division is:", result)
    else:
        print("Invalid choice. Please try again.")

calculator()
