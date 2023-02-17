# Number be expressed as a sum of two prime numbers.

N = int(input())
prime_numbers = []
for i in range(2, N):
    count = 2
    for j in range(2, i // 2 + 1):
        if(i % j == 0):
            count += 1
    if(count == 2):
        prime_numbers.append(i)

for i in range(len(prime_numbers)):
    for j in range(i+1, len(prime_numbers)):
        if(prime_numbers[i] + prime_numbers[j] == N):
            print("The {} can be expressed as the sum of {} and {}".format(N, prime_numbers[i], prime_numbers[j]))