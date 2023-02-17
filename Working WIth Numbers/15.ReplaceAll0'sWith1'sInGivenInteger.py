# Replace All 0’s With 1 In A Given Integer.

num = int(input())
N = num

# using inbuilt method
num = str(num)
print(num.replace('0', '1'))

# using loop
n = ""
while(N != 0):
    r = N % 10
    if(r == 0):
        r = 1
    n += str(r)
    N //= 10
print(n[::-1])