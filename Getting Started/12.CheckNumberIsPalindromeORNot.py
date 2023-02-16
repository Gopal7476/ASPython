# Check Whether or Not the Number is a Palindrome.

num = int(input())
reverse_num = int(str(num)[::-1])
if(num == reverse_num):
    print(num," is a Palindrome Number")
else:
    print(num," is not a Palindrome Number")