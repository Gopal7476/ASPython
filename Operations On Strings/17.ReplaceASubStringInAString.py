string = input()
substring_to_replace = input()
substring_which_replace = input()

# using buildin method
print(string.replace(substring_to_replace, substring_which_replace))

# using loop
ans = ""
a = len(substring_to_replace)
c = 0
for i in range(len(string)-(a-1)):
    if(string[i:a+i] == substring_to_replace):
        ans += substring_which_replace
        c += a-1
    else:
        ans += string[c]
    c += 1
print(ans)