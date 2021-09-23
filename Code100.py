"""
check if a Number Is Positive Or Negative
"""
##a=int(input())
##if a==0:
##    print("The number is Zero")
##elif a<0:
##    print("The number is negative")
##else:
##    print("The number is positive")


"""
Check Whether a Number is Even or Odd
"""
##a=int(input())
##if a%2==0:
##    print("Number is even")
##else:
##    print("Number is odd")


"""
Find the Sum of First N Natural Numbers
"""
##a=int(input())
##c=a*((a+1)//2)
##print("Sum is:",c)
##
##a=int(input())
##c=0
##for i in range(1,a+1):
##    print(c,"+",i)
##    c+=i
##print("Sum is:",c)
##
##a=int(input())
##c=0
##while a!=0:
##    c+=a
##    a-=1
##print("Sum is:",c)


"""
Find the Sum of First N Natural Numbers
"""
##a=int(input())
##c=0
##for i in range(a+1):
##    c+=i
##print("Sum of numbers:",c)
##
##a=int(input())
##c=0
##while a>=1:
##    c+=a
##    a-=1
##print("Sum of numbers:",c)


"""
find the sum of numbers in a given range
"""
##a,b=map(int,input().split())
##c=0
##for i in range(a,b+1):
##    c+=i
##print("Sum of these numbers",a,"to",b,"is :",c)


"""
Finding Fibonacci Sequence
"""
##a=int(input())
##b,c=0,1
##if a<0:
##    print("Incorrect Input")
##elif a==0:
##    print(a)
##elif a==1 or a==2:
##    print(1)
##else:
##    print(b,c,end=" ")
##    for i in range(2,a):
##        d=b+c
##        b=c
##        c=d
##        print(d,end=" ")      
      
      
"""
Find Greatest of Two Numbers
"""
##a,b=map(int,input().split())
##if (a>b):
##    print(a,"is larger number")
##else:
##    print(b,"is larger number")


"""
Find the Largest Number Among Three Numbers
"""
##a,b,c=map(int,input().split(" "))
##if ((a>b) and (a>c)):
##    print(a,"is larger number")
##elif (b>c):
##    print(b,"is larger number")
##else:
##    print(c,"is larger number")



"""
Check Year is a Leap Year or Not
"""
##a=int(input())
##if (((a%4==0) and (a%100!=0)) or (a%400==0)):
##    print(a,"is a Leap Year")
##else:
##    print(a,"is Not a Leap Year")



"""
check if the given number is Prime or not
"""
##a=int(input())
##c=0
##for i in range(1,a+1):
##    if a%i==0:
##        c+=1
##if c==2:
##    print("The given number",a,"is prime")
##else:
##    print("The given number",a,"is not prime")
##
##
##a=int(input())
##b=1
##c=0
##while b<=a+1:
##    if a%b==0:
##        c+=1
##    b+=1
##if c==2:
##    print("The given number",a,"is prime")
##else:
##    print("The given number",a,"is not prime")


"""
Print Prime Numbers In a Given Range
"""
##a,b=map(int,input().split())
##for i in range(a,b+1):
##    c=0
##    for j in range(1,i+1):
##        if i%j==0:
##            c+=1
##    if c==2:
##        print("prime numbers between",a,"to",b,":",i)
##
##a,b=map(int,input().split())
##e=a
##while a<=b:
##    d=1
##    c=0
##    while d<=a:
##        if a%d==0:
##            c+=1
##        d+=1    
##    if c==2:
##        print("prime numbers between",e,"to",b,":",a)
##    a+=1    
   

"""
Find Sum Of Digits Of a Number
"""
##a=int(input())
##c=0
##while a:
##    r=a%10
##    a=a//10
##    c+=r
##print(c)


"""
find the Reverse of a given number​
"""
##a=int(input())
##c=0
##while a:
##    r=a%10
##    a=a//10
##    c=c*10+r
##print(c)    



"""
Find a Number is Palindrome or not
"""
##a=int(input())
##b=a
##c=0
##while a!=0:
##    r=a%10
##    a=a//10
##    c=c*10+r
##if b==c:
##    print("%d is a palindrome number"%(b))
##else:
##    print(b,"is not a palindrome number")



"""
Find a Number is Armstrong or not
"""
##a=int(input())
##b=e=a
##c=d=0
##while a!=0:
##    r=a%10
##    c+=1
##    a=a//10
##while b!=0:
##    r=b%10
##    d+=pow(r,c)
##    b=b//10
##if e==d:
##    print("%d is a armstrong number"%(e))
##else:
##    print("%d is not a armstong number"%(e))


"""
Find Armstrong Numbers Between Two Intervals
"""
##a,b=map(int,input().split())
##c=d=g=0
##e=a
##f=b
##while a!=0:
##    r=a%10
##    c+=1
##    a=a//10
##while b!=0:
##    p=b%10
##    d+=1
##    b=b//10
##if c==d:
##    j=0
##    for i in range(e,f+1):
##        j=i
##        while j!=0:
##            q=j%10
##            g+=pow(q,c)
##            j=j//10
##        if g==i:
##            print(i,"number is armstrong ")
##        j=g=0


"""
find Fibonacci series up to n
"""
##a=int(input())
##b=0
##c=1
##print(b,c,end=" ")
##for i in range(2,a):
##    d=b+c
##    b,c=c,d
##    print(d,end=" ")


"""
Factorial of a Number
"""
##a=int(input())
##b=1
##for i in range(1,a+1):
##    b=i*b
##print(b)
##
##a=int(input())
##b=1
##while a!=0:
##    b=b*a
##    a-=1
##print(b)



"""
Find Power of a Number
"""
##a,b=map(int,input().split())
##c=pow(a,b)
##print(c)
##
##a,b=map(int,input().split())
##c=1
##for i in range(1,b+1):
##    c=c*a
##print(c)


"""
Find factors of a Number
"""
##a=int(input())
##for i in range(1,a+1):
##    if a%i==0:
##        print(i,end=" ")
##
##a=int(input())
##i=1
##while i<=a:
##    if a%i==0:
##        print(i,end=" ")
##    i+=1



"""
check whether a number is a Strong Number or not
"""
##a=int(input())
##b=a
##d=0
##while a!=0:
##    r=a%10
##    c=1
##    while r!=0:
##        c=c*r
##        if r==1:
##            d=d+c
##        r-=1 
##    a=a//10
##if b==d:
##    print("%d is a strong number"%(b))
##else:
##    print("%d is not a strong number"%(b))


"""
Perfect Number
"""
##a=int(input())
##b=1
##c=0
##while b<=(a//2):
##    if a%b==0:
##        c=c+b
##    b+=1    
##if a==c:
##    print("%d is a perfect number"%(a))
##else:
##    print("%d is not a perfect number"%(a))



"""
Automorphic number
"""
##n=int(input())
##x=n**2
##a=str(n)
##b=str(x)
##y=len(a)
##z=len(b)
##print("A",a,"B",b,"Y",y,"Z",z)
##print(z,"-",b.find(a),y)
##if(z-b.find(a)==y):
##    print("Automorphic")
##else:
##    print("Not automorphic number")




"""
Checking Whether the Number is Harshad or not
"""
##a=int(input())
##b=a
##c=0
##while a!=0:
##    r=a%10
##    c+=r
##    a=a//10
##if b%c==0:
##    print("%d is a harshad number"%b)
##else:
##    print("%d is not a harshad number"%(b))




"""
check Abundant Number
"""
##a=int(input())
##b=1
##c=0
##while b<=(a//2):
##    if a%b==0:
##        c+=b
##    b+=1
##if c>a:
##    print("Abundant Number")
##else:
##    print("Not a Abundant Number")



"""
check whether two numbers are Friendly Pair
"""
##a,b=map(int,input().split())
##c=d=1
##e=[]
##f=[]
##while c<=a:
##    if a%c==0:
##        e.append(c)
##    c+=1
##while d<=b:
##    if b%d==0:
##        f.append(d)
##    d+=1
##for i in range(len(e)):
##    for j in range(len(f)):
##        if (e[i]==f[j]) and (e[i]!=1 and e[j]!=1):
##            print("Abundancy index of %d and %d are"%(a,b),e[i],".so they are friendly pair.")



"""
find HCF of Two Numbers
"""
##def HCF(a,b):
##        while True:
##            if b==0:
##                return a
##            if a==0:
##                return b
##            if a>b:
##                a,b=b,a
##            b=b%a
##m,n=map(int,input().split())
##print(HCF(m,n))


"""
Program for LCM Of Two Numbers
"""
##def lcm(a,b):
##    t=2
##    res=1
##    while (a>=t and b>=t):
##        if a%t==0 and b%t==0:
##            a=a//t
##            b=b//t
##            res=res*t
##        else:
##            t+=1
##    return res*a*b
##a,b=map(int,input().split())
##print(lcm(a,b))



"""
Find the GCD of Two Numbers
"""
##def GCD(a,b):
##    while True:
##        if a==0:
##            return b
##        if b==0:
##            return a
##        if a>b:
##            a,b=b,a
##        b=b%a
##m,n=map(int,input().split())
##print(GCD(m,n))



"""
Binary To Decimal Conversion
"""
##a=int(input())
##dec=0
##base=1
##while a!=0:
##    r=a%10
##    dec+=r*base
##    a=a//10
##    base=base*2
##print(dec)    



"""
binary to octal conversion
"""
##Bin_num = 0b101
##Oct_num = oct(Bin_num)
##print('Number after conversion is :' + str(Oct_num))



"""
decimal to binary conversion
"""
##a=int(input())
##c=0
##while a!=0:
##    c=a%2
##    a=a//2
##    print(c)


"""
decimal to octal conversion
"""
##a=int(input())
##c=oct(a)
##print(c)


"""
Octal To Binary Conversion
"""
##a=0o564
##c=bin(a)
##print(c)


"""
octal to decimal conversion
"""
##a=0o512
##c=oct(a)
##print(a)


"""
find out the quadrant in which the given co-ordinate lie
"""
##x,y=map(int,input().split())
##if (x>0 and y>0):
##    print("Frist quadrant")
##elif (x<0 and y>0):
##    print("Second quadrant")
##elif (x<0 and y<=0):
##    print("Third quadrant")
##else:
##    print("Fourth quadrant")


"""
Permutations In Which N People Can Occupy R Seats In A Classroom
"""
##a,b=map(int,input().split())
##c=d=1
##e=a-b
##while a!=0:
##    c=c*a
##    a-=1
##while e!=0:
##    d=d*e
##    e-=1
##print(c//d)


"""
Finding Maximum Number Of Handshakes
"""
##a=int(input())
##b=((a-1)/2)
##c=a*b
##print(int(c))
    
