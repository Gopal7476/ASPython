# Binary to Decimal Conversion

binary = int(input())
binary_value = binary

# using loop
decimal = 0
base = 1
while(binary != 0):
    r = binary % 10
    decimal = decimal + r * base
    base *= 2
    binary //= 10
print("The decimal value of {} is {}".format(binary_value, decimal))

# using built-in method
print("The decimal value of {} is {}".format(binary_value, int(str(binary_value),2)))