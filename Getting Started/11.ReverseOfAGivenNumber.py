# Find the Reverse of a Number.

num = int(input())
reverse_num = 0
while(num != 0):
    r = num % 10
    reverse_num = reverse_num * 10 + r
    num //= 10
print(reverse_num)