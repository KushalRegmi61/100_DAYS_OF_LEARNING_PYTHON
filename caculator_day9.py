cond1 = True
cond2 = True
def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2
def modulo(n1,n2):
    return n1%n2
dict = {'+': add,
        '-': substract,
        '/': divide,
        '*': multiply,
        '%': modulo       
    }
for key in dict:
    print(key)
while cond1:    
    num1 = float(input("enter 1st no."))
    num2 = float(input("enter 2nd no."))
    operation = input("enter the operation symbol you want to perform:")    
    function = dict[operation]
    ans_1 = function(num1, num2)
    print(num1, operation , num2, "=", ans_1)
    while cond2:
        a = input("type y to continue calculating with previous operation and type n to start new operation")
        if a == "n":
            cond2 = False
        else:
            num3 =float(input("enter 3st no."))
            opt = input("enter the operation you want to perform")
            fnct = dict[opt]
            ans = fnct(ans_1,num3)
            print(ans_1,opt,num3, "= ",ans)
            ans_1 = ans       
    b = input("do you want to continue:")
    if b == "no":
        cond1 = False

    