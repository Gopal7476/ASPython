# Check Whether or Not the Number is a Perfect Number.

num = int(input())
sum_of_factors = 0
for i in range(1, num//2 + 1):
    if(num%i == 0):
        sum_of_factors += i
if(sum_of_factors == num):
    print(num," is a Prefect Number")
else:
    print(num," is Not a Prefect Number")