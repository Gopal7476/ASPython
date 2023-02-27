def palindrome_number(n):
    a = n
    ans = 0
    while(n != 0):
        r = n % 10
        ans = ans*10 + r
        n //= 10
    if(ans == a):
        return True

arr = [211, 2006, 3553, 6464, 715, 4334]
max_element = arr[0]
for i in range(len(arr)):
    if(palindrome_number(arr[i]) and max_element < arr[i]):
        max_element = arr[i]
print(max_element)
