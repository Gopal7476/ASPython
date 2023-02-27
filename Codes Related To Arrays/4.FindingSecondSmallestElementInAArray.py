import math
arr = [10, 58, 47, 69, 98, 12, 5, 8, 14, 1]

# using buildin method
arr.sort()
print(arr[1])

# using loop
min_element1 = min_element2 = math.inf
for i in range(len(arr)):
    if(min_element1 > arr[i]):
        min_element2 = min_element1
        min_element1 = arr[i]
    elif(min_element2 > arr[i] and min_element1 != arr[i]):
        min_element2 = arr[i]
print(min_element2)
    
