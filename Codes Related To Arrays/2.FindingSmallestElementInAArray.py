arr = [10, 58, 47, 69, 98, 12, 5, 8, 14, 1]

# using the buildin method
arr.sort()
print(arr[0])

print(min(arr))

# using loop
min_element = arr[0]
for i in range(1, len(arr)):
    if (min_element > arr[i]):
        min_element = arr[i]
print(min_element)