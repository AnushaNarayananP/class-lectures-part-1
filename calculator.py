from basic import *

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
n=input("type + for addition ,type - for subtraction,type * for multiplication and type / for division")
if n=="+":
    print(add(a,b))
elif n=='-':
    print(sub(a,b))
elif n=='*':
    print(mult(a,b))
elif n=='/':
    print (div(a,b))   
else:
    print("This symbol",n,"cannot be computed in basic calculator")           