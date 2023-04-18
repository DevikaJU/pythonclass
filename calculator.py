x=int(input("Enter your first number:"))
operator=input("Enter your Operator:(+,-,*,/,%):")
y=int(input("Enter your second number:"))

if operator=="+":
    print(x+y)
elif operator=="-":
    print(x-y)
elif operator=="*":
    print(x*y)
elif operator=="/":
    print(x/y)
elif operator=="%":
    print(x%y)
else:
    print("Operation not defined")
