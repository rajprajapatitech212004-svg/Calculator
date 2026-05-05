a = float(input("Enter First Number :"))
b = float(input("Enter Second Number :"))
operation = input("Enter operation ( + , - , * , / , // , % , ** ): ")

if operation == "+" :
    print("Result :", a + b)
    
elif operation == "-" :
    print("Result :", a - b)
    
elif operation == "*" :
    print("Result :", a * b)
    
elif operation == "/" :
    print("Result :", a / b)
    
elif operation == "//" :
    print("Result :", a // b)
    
elif operation == "%" :
    print("Result :", a % b)
    
elif operation == "**" :
    print("Result :", a ** b)
    
else:
    print("Invalid Operation")





