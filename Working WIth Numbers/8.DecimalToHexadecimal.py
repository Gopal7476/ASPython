# Decimal to Hexadecimal Conversion.

decimal = int(input())
decimal_value = decimal
hexadecimal = ""
while(decimal > 0):
    r = decimal % 16
    if(r < 10):
        hexadecimal += str(r)
    else:
        hexadecimal += str(chr(55 + r))
    decimal //= 16
print("The hexadecimal value of {} is {}".format(decimal_value,hexadecimal[::-1])) 

   