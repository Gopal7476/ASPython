# Binary to Octal Conversion.

def bin_to_dec(n):
    dec = 0
    base = 1
    while(n != 0):
        r = n % 10
        dec = dec + r * base
        base *= 2
        n //= 10
    return dec

def dec_to_oct(n):
    oct = ""
    while(n > 0):
        r = n % 8
        oct += str(r)
        n //= 8
    return oct[::-1]

binary = int(input())
decimal = bin_to_dec(binary)
octal = int(dec_to_oct(decimal))
print("The octal value of {} is {}".format(binary, octal))
