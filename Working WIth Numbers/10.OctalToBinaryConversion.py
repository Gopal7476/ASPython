# Octal To Binary Conversion.

def oct_to_dec(n):
    dec = 0
    base = 1
    while(n != 0):
        r = n % 10
        dec = dec + r * base 
        base *= 8
        n //= 10
    return dec

def dec_to_bin(n):
    bin = ""
    while(n > 0):
        r = n % 2
        bin += str(r)
        n //= 2
    return bin[::-1]

octal = int(input())
decimal = oct_to_dec(octal)
binary = dec_to_bin(decimal)
print("The binary value of {} is {}".format(octal, binary))