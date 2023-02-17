# LCM Of Two Numbers.

def HCF(n1, n2):
    if(n2 == 0):
        return n1
    return HCF(n2, n1%n2)

num1 = abs(int(input()))
num2 = abs(int(input()))
print("LCM of",num1,"and",num2,"is:",((num1 * num2) // HCF(num1, num2)))