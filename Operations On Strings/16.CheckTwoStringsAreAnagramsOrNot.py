string1 = input().lower()
string2 = input().lower()
if(sorted(string1) == sorted(string2)):
    print(string1, "and", string2, "are anagrams")
else:
    print(string1, "and", string2, "are not anagrams")