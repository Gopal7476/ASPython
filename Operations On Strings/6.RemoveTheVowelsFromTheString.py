string = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
ans = ""
for i in string:
    if i not in vowels:
        ans += i
print(ans)