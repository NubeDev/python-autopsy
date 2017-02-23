while True:
    message = """Help:
    quit - ends execution
    add - adds numbers
    """
    print(message)
    input = raw_input("Enter command: ")
    if input == "quit":
        break
    elif input == "add":
        num1 = raw_input("Enter num1: ")
        num2 = raw_input("Enter num2: ")
        print (int(num1) + int(num2))
        break
    else:
        print("Unknown operation!")
