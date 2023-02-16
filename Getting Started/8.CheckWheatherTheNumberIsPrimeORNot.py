# Check Whether a Number is a Prime or Not.
import math

num = int(input())

# using loop from 1 to num -----> o(n)
count = 0
for i in range(1, num+1):
    if(num % i == 0):
        count += 1
if(count == 2):
    print(num," is a Prime Number")
else:
    print(num," is not a Prime Number")

# using loop from 2 to num//2  -------> o(n/2)
c = 2
for i in range(2, num//2):
    if(num % i == 0):
        c += 1
if(c == 2):
    print(num," is a Prime Number")
else:
    print(num," is not a Prime Number")
