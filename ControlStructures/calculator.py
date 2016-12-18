while True:
    print("Options.")
    print("Enter 'add' to add two numbers")
    print("Enter 'sub' to subtract two numbers")
    print("Enter 'mul' to multiply two numbers")
    print("Enter 'div' to divide two numbers")
    print("Enter 'quit' to end the program")

    user_input = raw_input(':')

    if user_input == "quit":
        break
    elif user_input == "add":
        number1 = float(raw_input("Enter a number: "))
        number2 = float(raw_input("Enter another number: "))
        result = str(number1 + number2)
    elif user_input == "sub":
        number1 = float(raw_input("Enter a number: "))
        number2 = float(raw_input("Enter another number: "))
        result = str(number1 - number2)
    elif user_input == "mul":
        number1 = float(raw_input("Enter a number: "))
        number2 = float(raw_input("Enter another number: "))
        result = str(number1 * number2)
    elif user_input == "div":
        number1 = float(raw_input("Enter a number: "))
        number2 = float(raw_input("Enter another number: "))
        result = str(number1 / number2)
    else:
        print("Unknown input")

    print("The answer is " + result)
