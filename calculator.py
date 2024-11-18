def calculator (num1, num2, operation):
    num1 = int(input("Enter first Number: "))
    print("operations: ")
    print("1. + ")
    print("2. - ")
    print("3. * ")
    print("4. / ")
    operation = int(input("choose operation(1/2/3/4): "))
    num2 = int(input("Enter second number: "))

    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        if num2 == 0:
            return ValueError("Can't divide by zero!")
        return num1 / num2
    else:
        return ValueError("Invalid operation!...")
    
print(calculator(1, 2, 3))