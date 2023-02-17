# Decimal to binary conversion.

decimal = int(input())
decimal_value = decimal
binary = ""
while(decimal > 0):
    r = decimal % 2
    binary += str(r)
    decimal //= 2
print("The binary value of {} is {}".format(decimal_value,binary[::-1]))
