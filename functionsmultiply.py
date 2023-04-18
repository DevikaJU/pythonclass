
def add(value1,value2):
    return value1+value2

def prod(value1,value2):
    return value1*value2



operation=input("enter the operation:")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print("The answer is\t")

if operation=='+':
    ans =add(a,b)
    print(ans)

elif operation=='*':
    product= prod(a,b)
    print(product)

def add(x,y=10):
    print(x+y)

add(10)