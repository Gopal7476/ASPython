arr = [10, 58, 47, 69, 98, 12, 5, 8, 14, 1]

# using buildin methods
arr.sort()
print(arr[-1])

print(max(arr))

# using loop
max_element = arr[0]
for i in range(1, len(arr)):
    if(max_element < arr[i]):
        max_element = arr[i]
print(max_element)