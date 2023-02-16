# Check for Perfect Square.
import math

num = int(input())
if((int(math.sqrt(num)))*(int(math.sqrt(num))) == num):
    print(num," is a Prefect Square")
else:
    print(num," is Not a Prefect Square")