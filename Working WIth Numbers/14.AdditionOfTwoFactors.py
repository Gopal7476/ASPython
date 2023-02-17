# Addition of two fractions.

def hcf(n1, n2):
    if(n2 == 0):
        return n1
    return hcf(n2, n1 % n2)

num1, den1 = map(int,input().split())
num2, den2 = map(int,input().split())

lcm = (den1 * den2) // hcf(den1, den2) 
fraction = (num1 * den2) + (num2 * den1)
print(fraction,"/",lcm)