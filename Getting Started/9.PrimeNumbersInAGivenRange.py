# Find the Prime Numbers in a Given Range.

starting_value = int(input())
ending_value = int(input())
for i in range(starting_value, ending_value + 1):
    count = 2
    for j in range(2, i//2 + 1):
        if(i % j == 0):
            count += 1
    if(count == 2):
        print(i,end=" ")
    