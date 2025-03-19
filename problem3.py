a=float(input("Enter the First Number : "))
b=float(input("Enter The second Number : "))
operation=(input("enter an operator (+,*,-,/): "))

if operation=="+":
    result=a+b
elif operation=="*":
    result=a*b
elif operation=="-":
    result=a-b
elif operation=="/":
    result=a/b
else:
    "You entered the Wrong Operator"
print(f"{result}")