string = input()

# using buildin method
print(string[::-1])

# using loop
ans = ""
for i in range(len(string)-1, -1, -1):
    ans += string[i]
print(ans)