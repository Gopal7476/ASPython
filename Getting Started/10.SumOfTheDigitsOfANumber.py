# Find the sum of the Digits of a Number.

num = int(input())
sum_of_digits = 0
while(num != 0):
    r = num % 10
    sum_of_digits += r
    num //= 10
print(sum_of_digits)