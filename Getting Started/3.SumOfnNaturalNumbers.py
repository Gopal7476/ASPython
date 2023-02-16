# Find the Sum of The First N Natural Numbers.

N = int(input())

# using loop
sum_of_numbers = 0
for i in range (1,N+1):
    sum_of_numbers += i
print(sum_of_numbers)

# using math
print((N*(N+1))//2)