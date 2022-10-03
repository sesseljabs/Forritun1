OPERATORS = "+-*/"
PROMPT = "Enter an equation: "
'''
"Invalid operator"
"Invalid operands"
"Can't divide by 0"
'''

statement = input(PROMPT)

while statement!="q":

    first,op,second = statement.split(" ")
    total = 0
    
    if first.isdigit() and second.isdigit():
        first = int(first)
        second = int(second)
        if op == "+":
            total = first + second
        elif op == "-":
            total = first - second
        elif op == "*":
            total = first * second
        elif op == "/":
            if second != "0":
                total = first / second
            else:
                total = "Can't divide by 0"
        else:
            total = "Invalid operator"
    else:
        total = "Invalid operands"


    if str(total).replace(".","").replace("-","").isdigit(): # checking if it's numbers or a string
        print(f"Result: {round(total, 2):.2f}")
    else:
        print(f"{total}")

    statement = input(PROMPT)
