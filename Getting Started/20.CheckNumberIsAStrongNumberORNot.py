# Check Whether or Not the Number is a Strong Number.

def factorial(n):
    if(n == 1):
        return 1
    return n*factorial(n-1)

num = int(input())
n = num
sum_of_numbers = 0
while(num != 0):
    r = num % 10
    sum_of_numbers += factorial(r)
    num //= 10
if(n == sum_of_numbers):
    print(n," is a Strong Number")
else:
    print(n," is not a Strong Number")