# Find the Power of a Number.
import math

num, power = map(int,input().split(" "))

# using math library functions
print(int(math.pow(num, power)))

# using loop
ans = 1
for i in range(1, power + 1):
    ans *= num
print(ans)