string = input()
ans = ""
for i in string:
    if(i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        ans += i
print(ans)