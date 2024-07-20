def calculator():
    num1= float(input("enter a number:"))
    operator=input("enter an operator(+,-,*,/):")
    num2=float(input("enter a number:"))

    if operator== '+':
        result=num1+num2
    elif operator=='-':
        result=num1-num2
    elif operator=='*':
        result=num1*num2
    elif operator=='/':
        if num2 !=0:
            result=num1/num2
        else:
            result="invalid division"
    else:
        result="wrong operator"
    print('Result:',result)
calculator()



