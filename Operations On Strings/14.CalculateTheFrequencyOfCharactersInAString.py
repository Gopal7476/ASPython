string = input()
dict = {}
for i in string:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)
