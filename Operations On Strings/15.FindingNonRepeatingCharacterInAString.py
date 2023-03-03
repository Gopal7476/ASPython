string = input()
dict = {}
for i in string:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for j in dict:
    if(dict[j] == 1):
        print(j, end="")