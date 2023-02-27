arr = [10, 58, 47, 69, 98, 12, 5, 8, 14, 1]

# using buildin method
arr.sort()
print(arr[0:len(arr)//2] + arr[len(arr):len(arr)//2-1:-1])

# using loop
ans = []
for i in range(len(arr)//2):
    ans.append(arr[i])
print(ans + arr[len(arr):len(arr)//2-1:-1])
