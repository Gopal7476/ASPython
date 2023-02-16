# Check Whether or Not the Number is an Abundant Number.

num = int(input())
sum_of_factors = 0
for i in range(1, num//2 + 1):
    if(num%i == 0):
        sum_of_factors += i
if(num < sum_of_factors):
    print(num," is a Abundant Number")
else:
    print(num," is not a Abundant Number")