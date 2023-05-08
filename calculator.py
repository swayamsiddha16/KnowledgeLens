# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def quotient(a,b):
#     return a/b
# def calc(sign):
#     num1=int(input())
#     num2=int(input())
#     result=0
#     if sign == "+":
#         result=add(num1,num2)
#         print("adding two nos",result)
#         # result=add(num1,num2)
#     if sign == "-":
#         result=add(num1,num2)
#         print("adding two nos",result)
        
#     if sign == "*":
#         result=multiply(num1,num2)
#         print("multiplying two nos",result)
        
#     if sign=="/":
#         result=multiply(num1,num2)
#         print("multiplying two nos",result)
       

# signInput=str(input("Enter the sign : "))
# calc(signInput)


#or taking list as n input
def add(l,n):
    sum=0
    for i in range (0,n):
        sum += l[i]
    return sum
def sub(l,n):
    diff=0
    for i in range (0,n):
        diff -= l[i]
    return diff
def pro(l,n):
    prod=1
    for i in range(0,n):
        prod=prod*l[i]
    return prod
def quo(l,n):
    quot=1
    for i in range(0,n):
        quot=quot/l[i]
    return quot
def calc(sign):
    l=[]
    n=int(input("Enter the size of the list: "))
    for i in range(0,n):
        l.append(int(input()))
    result=0
    if sign=="+":
        result=add(l,n)
        print("adding  nos: ",result)
    if sign=="-":
        result=sub(l,n)
        print("subtracting  nos: ",result)
    if sign=="*":
        result=pro(l,n)
        print("multipying  nos: ",result)
    if sign=="/":
        result=quo(l,n)
        print("quotient of  nos: ",result)
    
signInput=str(input("Enter the sign : "))
calc(signInput)



    