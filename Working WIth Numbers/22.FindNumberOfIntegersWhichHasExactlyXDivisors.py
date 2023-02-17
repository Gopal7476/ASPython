# find number of integers which has exactly x divisors.

num = int(input())
divisor = int(input())
c = 0
for i in range(1, num + 1):
    count = 0
    for j in range(1, i + 1):
        if(i % j == 0):
            count += 1
    if(count == divisor):
        c += 1
print(c)