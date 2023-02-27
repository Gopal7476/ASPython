arr = [10, 20, 30, 10, 50, 20, 40]

# using dictionary
dict = {}
for i in range(len(arr)):
    if arr[i] in dict.keys():
        dict[arr[i]] += 1
    else:
        dict[arr[i]] = 1

for j in dict:
    if(dict[j] == 1):
        print(j, end=" ")