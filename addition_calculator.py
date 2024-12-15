while True:
    try:
        number1 = int(input("What is the first number? "))
        number2 = int(input("What is the second number? "))
        print("Sum of those values is:", (number1+number2))
        break
    except ValueError:
        print("Enter numbers!")