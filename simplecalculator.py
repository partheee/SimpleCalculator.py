#Simple Python Calculator for Beginners...
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if (choice>=1 and choice<=4):
        print("Enter two numbers: ")
        num1 = int(input("Enter the First Number: "))
        num2 = int(input("Enter the Second Number: "))
        #add two numbers
        if choice == 1:
            sum = num1 + num2
            print("Result = ", sum)
            exit()
        elif choice == 2:
        #subtract two numbers    
            sub = num1 - num2
            print("Result = ", sub)
            exit()
        #maltiply two numbers    
        elif choice == 3:
            mul = num1 * num2
            print("Result = ", mul)
            exit()
        #division of two numbers    
        else:
            div = num1 / num2
            print("Result = ", div)
            exit()
    elif choice == 5:
        exit()
    else:
        print("Wrong input..!!")
        exit()
