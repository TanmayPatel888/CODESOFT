
def calculator():
    
    print("Welcome To My Python Calculator")

    num1 = float(input("Enter first number:"))
    operator = input("choose the operation(*,-,+,/):")
    num2 = float(input("Enter Second number:"))
    if operator == '*':
        result = num1 * num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '+':
        result = num1 + num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "It cannot be divided by zero!"
    else:
        return "Invalid operator please choose from this (*,-,+,/)"

    return f" ❇️   Result: {num1} {operator} {num2} = {result}"
print(calculator())
    


