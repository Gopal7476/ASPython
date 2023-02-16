# Check Whether a Given Number is an Armstrong Number or Not.
import math 

num = int(input())
n=num
length = len(str(num))
sum_of_numbers = 0
while(num != 0):
    r = num % 10
    sum_of_numbers += math.pow(r, length)
    num //= 10
if(n == sum_of_numbers):
    print(n," is a Armstrong Number")
else:
    print(n," is not a Armstrong Number")