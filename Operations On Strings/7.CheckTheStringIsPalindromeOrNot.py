string = input()

# using buitin methods
st = string[::-1]
if(st == string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")

# using loop
ans = ""
for i in range(len(string)-1, -1, -1):
    ans += string[i]
if(ans == string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")