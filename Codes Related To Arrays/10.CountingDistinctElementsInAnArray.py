arr = [10, 20, 30, 10, 50]
a = arr

# using buildin method
print(len(set(arr)))

# using dictionary
dict = {}
for i in range(len(a)):
    if arr[i] in dict.keys():
        dict[arr[i]] += 1
    else:
        dict[arr[i]] = 1
print(len(dict.keys()))