string = input()

# using buildin method
print(string.swapcase())

# using loop
ans = ""
for i in string:
    if(i.isupper()):
        i = i.lower()
        ans += i
    else:
        i = i.upper()
        ans += i
print(ans)