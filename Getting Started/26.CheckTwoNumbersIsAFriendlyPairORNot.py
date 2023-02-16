# Check Whether or Not the Two Numbers  are Friendly Pairs.
def factors(n):
    sum_of_factors = 0
    for i in range(1, n//2 + 1):
        if(n%i == 0):
            sum_of_factors += i
    return sum_of_factors

num1, num2 = map(int,input().split())
if((factors(num1)//num1) == (factors(num2)//num2)):
    print(num1,num2," are Friendly Pair")
else:
    print(num1,num2," are not Friendly Pair")