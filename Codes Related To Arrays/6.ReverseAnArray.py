arr = [10, 58, 47, 69, 98, 12, 5, 8, 14, 1]
a = arr

# using builtin method
print(arr[::-1])

# using loop
j = len(a) - 1
for i in range(len(a)//2):
    a[i],a[j] = a[j],a[i]
    j -= 1
print(a)