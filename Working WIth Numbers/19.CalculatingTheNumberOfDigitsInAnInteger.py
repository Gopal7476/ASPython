# calculate number of digits in an integer.

num = int(input())

# using inbuilt methods
print(len(str(num)))

# using loop
count = 0
while(num != 0):
    count += 1
    num //= 10
print(count)