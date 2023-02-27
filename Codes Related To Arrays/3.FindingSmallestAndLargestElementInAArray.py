arr = [10, 58, 47, 69, 98, 12, 5, 8, 14, 1]

# using builtin methods
print("Minimum Element in the arrray: ", min(arr))
print("Maximum Element in the array: ", max(arr))

arr.sort()
print("Minimum Element in the array: {} and Maximum Element in the array: {}".format(arr[0], arr[len(arr) - 1]))

# using loop
min_element = arr[0]
max_element = arr[0]
for i in range(1, len(arr)):
    if(min_element > arr[i]):
        min_element = arr[i]
    if(max_element < arr[i]):
        max_element = arr[i]
print("Minimum Element in the array: {} and Maximum Element in the array: {}".format(min_element, max_element))        