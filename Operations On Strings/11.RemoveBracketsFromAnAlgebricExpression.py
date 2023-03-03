string = input()
ans = ""
for i in string:
    if(i == '(' or i ==')' or i == '{' or i == '}' or i == '[' or i == ']'):
        continue
    else:
        ans += i
print(ans)