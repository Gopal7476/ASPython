# Factorial of a Number.

num = int(input())

# using loop
factorial_number = 1
for i in range(1, num+1):
    factorial_number *= i
print(factorial_number)

# using recursive function
def fact(n):
    if(n == 1):
        return 1
    return n*fact(n-1)

print(fact(num))