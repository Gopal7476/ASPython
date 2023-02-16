# Find the Armstrong Number in a given Range.
import math

starting_value = int(input())
ending_value = int(input())
for i in range(starting_value, ending_value + 1):
    n = i
    length = len(str(n))
    sum_of_numbers = 0
    while(i != 0):
        r = i % 10
        sum_of_numbers += math.pow(r, length)
        i //= 10
    if(sum_of_numbers == n):
        print(n,end = " ")
