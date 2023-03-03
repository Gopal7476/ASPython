string = input()
ans = list(string)
c = 0
for i in range(len(string)):
    if(c == 0 and string[i + 1] != ' '):
        ans[i] = string[i].upper()
        c += 1
    elif(string[i] == ' '):
        c = 0
        ans[i-1] = ans[i-1].upper()
    else:
        ans[i] = string[i]
ans[-1] = ans[-1].upper()
print("".join(ans))
