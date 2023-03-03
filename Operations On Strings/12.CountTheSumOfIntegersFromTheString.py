string = input()
sum_of_numbers = 0
for i in string:
    if(ord(i) >= 48 and ord(i) <= 57):
        sum_of_numbers += int(i)
print(str(sum_of_numbers))