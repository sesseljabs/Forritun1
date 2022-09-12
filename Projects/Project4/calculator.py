OPERATORS = "+-*/"
PROMPT = "Enter an equation: "
'''
"Invalid operator"
"Invalid operands"
"Can't divide by 0"
'''

equation = input(PROMPT)

while equation!="q":

    a,o,b = equation.split(" ")
    total = 0
    
    if a.isdigit() and b.isdigit():
        if o == "+":
            total = int(a) + int(b)
        elif o == "-":
            total = int(a) - int(b)
        elif o == "*":
            total = int(a) * int(b)
        elif o == "/":
            if b != "0":
                total = int(a) / int(b)
            else:
                total = "Can't divide by 0"
        else:
            total = "Invalid operator"
    else:
        total = "Invalid operands"


    if str(total).replace(".","").replace("-","").isdigit():
        print(f"Result: {round(total, 2):.2f}")
    else:
        print(f"{total}")

    equation = input(PROMPT)
