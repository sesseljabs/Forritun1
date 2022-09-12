OPERATORS = "+-*/"
PROMPT = "Enter an equation: "
'''
"Invalid operator"
"Invalid operands"
"Can't divide by 0"
'''

equation = input(PROMPT)

while equation!="q":
    #print(equation.isdigit())
    sum=0
    prevoperator = ""
    currentnum = ""

    for i in equation:
        print("sum:",sum,"currentnum",currentnum)
        if i.isdigit():
            print("is is digit %s"%i)
            currentnum+=i

        elif i in OPERATORS:

            print("i is %s operator"%i)

            if prevoperator == "+":
                sum += int(currentnum)
                print("add to sum lolol")

            elif prevoperator == "-":
                sum -= int(currentnum)

            elif prevoperator == "*":
                sum *= int(currentnum)

            elif prevoperator == "/":
                if i != 0:
                    sum /= int(currentnum)
                else:
                    print("Can't divide by 0")

            else:
                pass
            currentnum = ""
            prevoperator=i
            print()
        print()
    print(sum)

    equation = input(PROMPT)
