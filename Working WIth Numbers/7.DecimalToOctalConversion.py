# Decimal to octal conversion.

decimal = int(input())
decimal_value = decimal
octal = ""
while(decimal > 0):
    r = decimal % 8
    octal += str(r)
    decimal //= 8
print("The octal value of {} is {}".format(decimal_value,octal[::-1]))
