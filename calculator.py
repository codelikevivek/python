first = input("Enter First Digit: ")
operator = input("Enter Operator (+, -, *, /, %) : ")
second = input("Enter Second Digit: ")

first = int(first)
second = int(second)

if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
elif operator == '%':
    print(first % second)
else:
    print("Invalid operator")
