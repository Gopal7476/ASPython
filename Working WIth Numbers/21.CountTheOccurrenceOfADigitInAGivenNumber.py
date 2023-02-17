# count the Occurrence of a Digit in a given Number.

num = int(input())
n = num
digit = int(input())

# using strings and its inbuild function
N = str(num)
dig = str(digit)
print(N.count(dig))

# using loop
count = 0
while(num != 0):
    r = num % 10
    if(r == digit):
        count += 1
    num //= 10
print("In given number {} the digit {} occured in {}".format(n, digit, count))