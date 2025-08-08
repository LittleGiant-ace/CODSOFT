def calculator():
    print('"WELCOME"')
    print("You can get the answer to addition (+), subtraction (-), multiplication (*), or division (/) here.")

    sign = input("Please enter an arithmetic operator: ")
    
    try:
        value1 = int(input("Enter your first number: "))
        value2 = int(input("Enter your second number: "))

        if sign == '+':
            print("The result of the addition is:", value1 + value2)
        elif sign == '-':
            print("The result of the subtraction is:", value1 - value2)
        elif sign == '*':
            print("The result of the multiplication is:", value1 * value2)
        elif sign == '/':
            if value2 != 0:
                print("The result of the division is:", value1 / value2)
            else:
                print("Error: Cannot divide by zero")
        else:
            print("Invalid operator")
    except ValueError:
        print("Error: Please enter valid numbers.")

    print("THANK YOU\n")

while True:
    calculator()
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Goodbye!,have great day")
        break
