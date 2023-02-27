arr = [10, 58, 47, 69, 98, 12, 5, 8, 14, 1]

# using inbuild method
print(sum(arr))

# using loop
sum_of_elements = 0
for i in range(len(arr)):
    sum_of_elements += arr[i]
print(sum_of_elements)