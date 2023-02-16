# Find the Sum of the Numbers in a Given Range.

starting_value = int(input())
ending_value = int(input())
sum_of_values = 0
for i in range(starting_value,ending_value+1):
    sum_of_values += i 
print(sum_of_values)