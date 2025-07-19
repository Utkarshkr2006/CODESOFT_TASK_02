# Simple calculator with basic arthimatic operation from user input

def add(num1,num2): 
    return num1+num2

def subtract(num1,num2): 
    return num1-num2

def multiply(num1,num2): 
    return num1*num2

def divide(num1,num2):
    if num2 !=0:
        return num1/num2
    else:
        return "Error! Division by zero."

def average(num1,num2): 
    return (num1+num2)/2
  

while True:


    print("\n Please select an operation: \n" 
      "1. Addition \n" 
      "2. Subtraction \n"
      "3. Multiply \n"  
      "4. divide  \n" 
      "5. Average \n"
      "6.Exit \n")

    select=int(input("Select an operation from 1 to 6: "))
    if select==6:
        print("Exiting Calculator!")
        break

    number1=int(input("Enter your first number: "))
    number2=int(input("Enter your second number: "))



    if select==1:
        print(f" Result: {number1} + {number2} = ",add(number1,number2))

    elif select==2:
        print(f" Result: {number1} - {number2} = ",subtract(number1,number2))

    elif select==3:
        print(f" Result: {number1} x {number2} = ",multiply(number1,number2))

    elif select==4:
        print(f" Result: {number1} / {number2} = ",divide(number1,number2))

    elif select==5:
        print(f" Result: ({number1} + {number2})/2 = ",average(number1,number2))

    else:
        print("Invalid selection, please choose between 1 to 6")