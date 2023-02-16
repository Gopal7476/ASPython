# Check Whether or Not a Number is a Harshad Number.

num = int(input())
n = num
sum_of_digits = 0
while(num != 0):
    r = num%10
    sum_of_digits += r
    num //= 10
if(n%sum_of_digits == 0):
    print(n," is a Harshad Number")
else:
    print(n," is Not a Harshad Number")