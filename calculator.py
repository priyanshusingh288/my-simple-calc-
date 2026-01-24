operator = (input("+,-,/,* :"))
numb1 = float(input("enter the numb1 :"))
numb2 = float(input("enter the numb2 :"))

if operator == "+":
    result = numb1+numb2
    print(round(result,1))
elif operator == "-":
    result =numb1-numb2
    print(round(result,1))
elif operator == "/":
    result = numb1/numb2
    print(round(result,1))
elif operator == "*":
    result = numb1*numb2
    print(round(result,1))
else:
    print("operator is not valid")