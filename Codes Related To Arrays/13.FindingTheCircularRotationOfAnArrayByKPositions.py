arr = [10, 20, 30, 40, 50]
ab = arr
K = int(input())

# For right rotation
for i in range(K):
    arr.insert(0, arr.pop())
    print(arr)

# For left rotation
for j in range(K):
    ab.insert(len(ab)-1, ab.pop(0))
    print(ab)