def add(n1,n2):
    return(n1+n2)

def substract(n1,n2):
    return(n1-n2)

def multiply(n1,n2):
    return(n1*n2)

def divide(n1,n2):
    return(n1/n2) 

operations = {
    "+" : add,
    "-" : substract, 
    "*" : multiply,
    "/" : divide,

} 

num1=int(input("enter first number"))
num2=int(input("enter second number"))

for oper in operations:
    print(oper)
answer=0
symbol = input("pick the operations")  

if(symbol=="+"):
    answer=operations["+"](num1,num2)
elif (symbol=="-"):
    answer=operations["-"](num1,num2)
elif (symbol=="*"):
    answer=operations["*"](num1,num2)
else:
    answer=operations["/"](num1,num2)

print(f"{num1} {symbol} {num2} = {answer}")