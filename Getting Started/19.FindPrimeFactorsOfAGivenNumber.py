# Find the Prime Factors of a Number.

def prime(n):
    count = 2
    for i in range(2, n//2 + 1):
        if(n % i == 0):
            count += 1
    if(count == 2):
        return True
    return False

num = int(input())
for i in range(2, num + 1):
    if((num % i == 0) and prime(i)):
        print(i, end=" ")