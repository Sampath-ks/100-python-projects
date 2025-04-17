def basic_calculator():
    print("Welcome to the Calculator App!")           
    while True:
        a=int(input("Enter the first number:"))
        operator=input("Enter the operator(+,-,*,/):")
    
        b=int(input("Enter the second number:"))
        try:
            if operator=='+':
                print("Result=",a+b)
            elif operator=='-':
                print("Result=",a-b)
            elif operator=='*':
                print("Result=",a*b)
            elif operator=='/': 
                  if b==0:
                    print("Second number can not be zero since a number cannot be divided by zero")
                  else:
                    print("Result=",a/b)
            else:
                print("Invalid operator,try '+','-','*','/'")
                continue    
        except ValueError:
            print("please enter a valid number.")
        c=input("Do you want to re calculate (yes/no):").lower()
        
        if c!="yes":
            print("Thanks for using calculator!")
            break
basic_calculator()