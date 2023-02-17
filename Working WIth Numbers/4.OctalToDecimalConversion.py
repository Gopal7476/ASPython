# Octal To Decimal Conversion.

octal = int(input())
octal_value = octal

# using loop
decimal = 0
base = 1
while(octal != 0):
    r = octal % 10
    decimal = decimal + r * base 
    base *= 8
    octal //= 10
print("The decimal value of {} is {}".format(octal_value, decimal))

# using build-in method
decimal_value = int(str(octal_value), 8)
print("The decimal value of {} is {}".format(octal_value, decimal_value))