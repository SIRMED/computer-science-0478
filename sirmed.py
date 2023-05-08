print("Select from the following functions: ")
print("1- Positive Negative Check")
print("2- Number Comparison")
print("3- Even/Odd")
print("4- Calculator")
print("5- 3 Number Comparison")
print("6- Square Check")
print("7- Discount")
print("kill- End program")
print("")

selection = str(input("Selection: "))
program = "running"

while(program == "running"):
    if(selection == "1"):
        print("")
        print("Positive Negative Check")
        num = int(input("Enter Number: "))

        if(num > 0):
            print(num, "is positive")
        elif(num < 0):
            print(num, "is negative")
        else:
            print("The number is 0")
        print("")
        selection = str(input("Selection: "))
    elif(selection == "2"):
        print("")
        print("Number Comparison")
        print("Enter your numbers")
        num1 = int(input("Number 1:"))
        num2 = int(input("Number 2:"))

        if(num1 > num2):
            print(num1, "is bigger than", num2)
        elif(num2 > num1):
            print(num2, "is bigger than", num1)
        elif(num1 == num2):
            print("They are equal")
        else:
            print("Couldn't identify")
        print("")
        selection = str(input("Selection: "))
    elif(selection == "3"):
        print("")
        print("Even/Odd")
        print("Enter your number")
        num = int(input("Number: "))

        if(num%2):
            print(num, "is odd")
        else:
            print(num, "is even")
        print("")
        selection = str(input("Selection: "))
    elif(selection == "4"):
        print("")
        print("Calculator selected")
        print("Select from the following functions:")
        print("1- Addition")
        print("2- Subtraction")
        print("3- Multiplication")
        print("4- Division")
        print("5- Modulous")
        print("6- Exit")
        print("")

        op = str(input("Operation to do: "))
        calculatorRunning = "running"

        while(calculatorRunning == "running"):
            if(op == "1"):
                print("Addition")
                num1 = int(input("Number 1: "))
                num2 = int(input("Number 2: "))
                print(num1, "+", num2, "=", num1+num2)
                op = str(input("Operation to do: "))
            elif(op == "2"):
                print("Subtraction")
                num1 = int(input("Number 1: "))
                num2 = int(input("Number 2: "))
                print(num1, "-", num2, "=",num1-num2)
                op = str(input("Operation to do: "))
            elif(op == "3"):
                print("Multiplication")
                num1 = int(input("Number 1: "))
                num2 = int(input("Number 2: "))
                print(num1, "*", num2, "=",num1*num2)
                op = str(input("Operation to do: "))
            elif(op == "4"):
                print("Division")
                num1 = int(input("Number 1: "))
                num2 = int(input("Number 2: "))
                print(num1, "/", num2, "=",num1/num2)
                op = str(input("Operation to do: "))
            elif(op == "5"):
                print("Modulous")
                num1 = int(input("Number 1: "))
                num2 = int(input("Number 2: "))
                print(num1, "%", num2, "=",num1%num2)
                op = str(input("Operation to do: "))
            elif(op == "6"):
                print("Calculator Closed")
                print("")
                calculatorRunning = "not"
                selection = str(input("Selection: "))
            else:
                print("Select a valid operator")
                op = str(input("Operation to do: "))
    elif(selection == "5"):
        print("")
        print("3 Number Comparison")
        n1 = float(input("First number: "))
        n2 = float(input("Second number: "))
        n3 = float(input("Third number: "))

        if(n1 > n2 and n1 > n3):
            print(n1 , "is the largest")
        elif(n2 > n1 and n2 > n3):
            print(n2 , "is the largest")
        elif(n3 > n1 and n3 > n2):
            print(n3 , "is the largest")
        else:
            print("2 or more numbers are the same")

        if(n1 < n2 and n1 < n3):
            print(n1 , "is the smallest")
        elif(n2 < n1 and n2 < n3):
            print(n2 , "is the smallest")
        elif(n3 < n1 and n3 < n2):
            print(n3 , "is the smallest")
        else:
            print("2 or more numbers are the same")

        print("")
        selection = str(input("Selection: "))
    elif(selection == "6"):
        print("")
        print("Square check")
        l = float(input("Length of shape: "))
        w = float(input("Width of shape: "))
        a = l*w
        if(l == w):
            print("Your shape is a square with area: ", a)
        else:
            print("Your shape is not a square, it has an area: ", a)
        print("")
        selection = str(input("Selection: "))
    elif(selection == "7"):
        print("")
        print("Discount")
        total = float(input("Your total amount: "))
        if(total >= 1000):
            percent10 = (total/100)*10
            discounted = total-percent10
            print("You are eligible for a 10% discount")
            print("Your final amount is: ", discounted)
        else:
            print("You are not eligible for discount")
            
    elif(selection == "kill"):
        program = "not"
        print("")
        print("Goodbye!")
    else:
        print("")
        print("Please select a valid function")
        print("")
        selection = str(input("Selection: "))










