arr = [10, 30, 10, 20, 10, 20, 30, 10]

# using loop
a = arr
a = list(set(arr))
for i in range(len(a)):
    print(a[i], arr.count(a[i]))


# using hashmap/dictionary
dic = {}
for i in range(len(arr)):
    if arr[i] in dic.keys():
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1

for j in dic:
    print(j,dic[j])