# find HCF of Two Numbers.

def HCF(n1, n2):
    if(n2 == 0):
        return n1
    return HCF(n2,n1%n2)

num1 = int(input())
num2 = int(input())
print("HCF of",num1,"and",num2,"is:",HCF(abs(num1), abs(num2)))