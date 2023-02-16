# Check Whether or Not the Number is an Automorphic Number.
import math

num = int(input())
square_of_number = int(math.pow(num, 2))
n = int(str(square_of_number)[-len(str(num))::])
if(n == num):
    print(num," is a Automorphic Number")
else:
    print(num," is Not a Automorphic Number")