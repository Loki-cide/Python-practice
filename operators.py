operator = input("Enter an operator (+,-,*,/): ")
first = float(input("Enter 1st number: "))
second = float(input("Enter 2nd number: "))

if operator == "+":
    result = first + second
    print(result)
elif operator == "-":
    result = first - second
    print(result)
elif operator == "*":
    result = first * second
    print(result)
elif operator == "/":
    if second != 0:
        result = first / second
        print(result)
    else:
        input("Second number can not be zero when dividing.")
else:
    input("The operator is not correct.")