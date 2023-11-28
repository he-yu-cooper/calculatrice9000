history = []

def get_input():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    return num1, num2, operator

def calculate(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
    
    history.append((num1, operator, num2, result))
    return result

def show_history():
    for i, item in enumerate(history):
        num1, operator, num2, result = item
        print(f"{i+1}. {num1} {operator} {num2} = {result}")

def clear_history():
    history.clear()
    print("History has been cleared.")

while True:
    num1, num2, operator = get_input()
    result = calculate(num1, num2, operator)
    print("The result is: ", result)
    
    command = input("Enter 'h' to view history, 'c' to clear history, 'q' to quit the program: ")
    if command.lower() == 'h':
        show_history()
    elif command.lower() == 'c':
        clear_history()
    elif command.lower() == 'q':
        break
