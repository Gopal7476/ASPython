"""
program for (a+b)**2
"""
##a=int(input(""))
##b=int(input(""))
##c=((a**2)+(b**2)+(2*a*b))
##print(c)



"""
CONDITIONAL STATEMENTS
program for eligiblity
"""
##stream=str(input("enter the stream\t"))
##branch=str(input("enter the branch\t"))
##year=int(input("enter the year\t"))
##per=int(input("enter the percentage\t"))
##bc=int(input("enter the backlog\t"))
##gen=str(input("enter the gender\t"))
##if stream=="engg" and (branch=="cse" or "it" or "ece") and year==4 and per>=70 and bc==0 and gen=="male":
##    print("eligible")
##else:
##    print("not eligible")
##
##
##
##
##stream=str(input("enter the stream\t"))
##branch=str(input("enter the branch\t"))
##year=int(input("enter the year\t"))
##per=int(input("enter the percentage\t"))
##bc=int(input("enter the backlog\t"))
##gen=str(input("enter the gender\t"))
##if stream=="engg" and branch!="mech" and branch!="argi" and branch!="pert" and year==4 and per>=70 and bc==0 and gen=="male"):
##    print("eligible")
##else:
##    print("not eligible")




"""
program for checking the number is even or odd
"""
##n=int(input(""))
##if n%2==0:
##    print(n,"is EVEN")
##else:
##    print(n,"is ODD")




"""
program for checking the number is even or odd on test cases
"""
##T=int(input(""))
##for i in range(T):
##    n=int(input(""))
##    if n%2==0:
##        print(n,"is EVEN")
##    else:
##        print(n,"is ODD")



"""
program for checking the number is +ve or -ve or zero
"""
##n=int(input(""))
##if n==0:
##    print(n,"is ZERO")
##elif n>0:
##    print(n,"is POSITIVE NUMBER")
##else:
##    print(n,"is NEGATIVE NUMBER")



"""
LOOPS
programs for basic loops concept
contol statement --> for ,while
continue,break,pass
"""
##n=int(input(""))
##for i in range(n+1):
##    print(i,end=" ")
##
##
##n=int(input(""))
##for i in range(1,n+1):
##    print(i)
##
##
##m,n=map(int,input("").split())
##for i in range(m,n+1):
##    print(i,end=" ")    
##
##
##m,n=map(int,input("").split())
##for i in range(n,m-1,-1):
##    print(i,end=" ")    
##
##
##m,n=map(int,input("").split())
##while (m<n+1):
##    print(m,end=" ")
##    m+=1
##
##m,n=map(int,input("").split())
##while (m-1<n):
##    print(n,end=" ")
##    n-=1
##
##
##m,n=map(int,input("").split())
##i=n
##while i>m:
##    print(i,end=" ")
##    i-=1
##
##m,n=map(int,input("").split())
##i=n
##while i>=m:
##    if (i%3==0):
##        i-=1
##        continue
##    print(i,end=" ")
##    i-=1
##
##
##m,n=map(int,input("").split())
##for i in range(m,n+1):
##    print(i,end=" ")
##    if i%4==0:
##        break
##    
##m,n=map(int,input("").split())
##for i in range(m,n+1):
##    print(i,end=" ")
##    if i%4==0 and i!=4:
##        break    



"""
else in loops

else of loop is exceuted when the loop is breaking naturally
"""
##m,n=map(int,input().split())
##while(m<=n): # withour break statement the loop is breaking it is called natural breaking
##    print(m,end=" ")
##    m+=1
##else:
##    print("HAI")
##
##m,n=map(int,input().split())
##while(m<=n): # withour break statement the loop is breaking it is called natural breaking
##    print(m,end=" ")
##    m+=1
##    if m%4==0: 
##        break
##else:
##    print("HAI")



"""
multiple tables
"""
##a=int(input(""))
##m,n=map(int,input("").split())
##for i in range(m,n+1):
##    print(a,"X",i,"=",a*i)

"""
mutiple tables of even divisibles
"""
##a=int(input(""))
##m,n=map(int,input("").split())
##for i in range(m,n+1):
##    if i%2==0:
##        print(a,"X",i,"=",a*i)
    
"""
multiple tables of odd divisibles
"""
##a=int(input(""))
##m,n=map(int,input("").split())
##for i in range(m,n+1):
##    if i%2!=0:
##        print(a,"X",i,"=",a*i)
##
##
##num=int(input(""))
##for i in range(2,21,2):
##    if i%2!=0:
##        continue
##    print(num,"X",i,"=",num*i)
##
##m,n=map(int,input().split())
##for i in range(1,n+1):
##    print(m,"X",i,"=",m*i)
##
##m,n,o=map(int,input().split())
##for i in range(n,o+1):
##    print(m,"X",i,"=",m*i)



##m,n,o=map(int,input().split())
##if n>o:
##    n,o=o,n
##for i in range(n,o+1):
##        print(m,"X",i,"=",m*i)


##m,n,o=map(int,input().split())
##p=1
##if n>o:
##    p=-1
##for i in range(n,o+p,p):
##    print(m,"X",i,"=",m*i)


"""
given number multiples does not exist
given number limit does not exist
"""
##m,n=map(int,input().split())
##for i in range(1,n+1):
##    if i%m==0:
##        continue
##    print(m,"X",i,"=",m*i)
##
##m,n=map(int,input().split())
##for i in range(1,n+1):
##    if m*i>n:
##       break
##    print(m,"X",i,"=",m*i)
    

"""
Reverse of a given number
"""
##num=int(input())
##while num:
##    r=num%10
##    num=num//10
##    print(r,end="")


"""
Counting the given number
"""
##num=int(input())
##c=0
##num=abs(num)
##while num:
##    num=num//10
##    c+=1
##print(c)    
    


"""
In given number no.of even digits and no.of odd digits
1234
1112
112
"""
##num=int(input())
##a=0
##b=0
##while num:
##    r=num%10
##    if r%2==0:
##        a+=1
##    else:
##        b+=1
##    num=num//10
##print(a,b)
##if a%2==0:
##    print("Even",end=" ")
##if b%2!=0:
##    print("Odd")
##if a%2!=0 and b%2==0:
##    print("Not Even Not Odd")
    


"""
if given number is 12345
print 24 135
"""
##n=12345
##a=b=c=d=0
##while n:
##    r=n%10
##    if r%2==0:
##        a=a*10+r
##    else:
##        b=b*10+r
##    n=n//10
##while a:
##    r=a%10
##    a=a//10
##    c=c*10+r
##while b:
##    r=b%10
##    b=b//10
##    d=d*10+r
##print(c,d)    
    


"""
check given each number is even print even(2468)
check given each number is odd print odd(1357)
check given each number is even but some given number is odd print even odd(1234)
check given each number is odd but some given number is even print odd even(12345)
"""    
##n=int(input())
##a=b=0
##c=n
##while n:
##    r=n%10
##    if r%2==0:
##       a=a*10+r
##    else:   
##       b=b*10+r
##    n=n//10
##if a%2==0 and b==0:
##    print("Even")
##elif b%2==1 and a==0:
##    print("Odd")
##else:
##    if c%2==0:
##        print("Even Odd")
##    else:
##        print("Odd Even")



"""
check the number is in the given value
12345 ---> 3 (is there in the given number so print True)
12345 ---> 7 (is not there in the given number so print False)
"""
##n,m=map(int,input().split())
##a=0
##while n:
##    r=n%10
##    if r==m:
##        a=r
##    n=n//10
##if a==m:
##    print("True")
##else:
##    print("False")




"""
check the given number in the order of even,odd,even,odd (or) odd,even,odd,even print Wave Form (1234)
if the number is in even odd even even (or) odd odd even odd print Not In Wave Form (2456)
"""
##num=int(input())
##d=num%10
##num=num//10
##while num:
##    r=num%10
##    num=num//10
##    if (d%2==0 and r%2==0) or (d%2==1 and r%2==1):
##        print("Not in a Form")
##        break
##    d=r
##else:
##    print("Wave Form")



"""
check if given number a is even then divide by 2 and b is multiply by 2
then ware if a is odd then add the b value
a=14 b=24
14/2  24*2 ---> 7/2  48*2 ---> 3/2  96*2 ---> 1  192
so add b values ware the a is odd --> 48 + 96 + 192 = 336 and multiplication of a and b = 14 * 24 = 336
"""
##a,b=map(int,input().split())
##t=u=0
##if a%2==1:
##    t=b
##while a!=0:
##    r=a//2
##    s=b*2
##    u=s
##    if r%2==1 and s%2==0:
##        t=t+u
##    a=r
##    b=s
##print(t)    



"""
if n=6 --> 6(E)//2 --> 3(O)*3+1 --> 10(E)//2 --> 5(O)*3+1 --> 16(E)//2 --> 8(E)//2 --> 4(E)//2 --> 2(E)//2 --> 1
"""
##n=int(input())
##while n>1:
##    print("N",n)
##    if n%2==0:
##        n=n//2
##    else:
##        n=n*3+1
##    n=n
##print("n",n)
       
        


"""
LCM of 2 numbers
"""
##a,b=map(int,input().split())
##s=1
##t=2
##while a:
##    if a%t==0 and b%t==0:
##        a=a//t
##        b=b//t
##        s*=t
##        print(t,a,b,s)
##    elif t>=a or t>=b:
##        s=s*a*b
##        break
##    else:
##        t=t+1
##print(s)        




"""
LCM of 2 number by the factors of second number
"""
##a,b=map(int,input().split())
##n=1
##while n:         # 1 (6,12)          # 1 (12,6)
##    c=b*n        # 12                # c=6*1= 6 , c=6*2=12
##    if c%a==0:   # 12%6==0 True      # 6%12==0 False, 12%12==0 True
##        print(c) # 12                # 6 NOT BREAKED so n=2, 12 BREAk
##        break
##    n+=1




"""
Function
function --> function defnition
             function call
types --> function with return type
          function without return type  
"""

"""
function without return type program so we use print statement
if we use without return type we can call by just without assign or print
"""
##def add(a,b):
##    print(a+b)
##
##a=10
##b=20
##add(a,b)


"""
function with return type program so we use return statement
if we use return type we can call by assign the value like result then print 
"""
##def add(a,b):
##    return a+b
##
##a=10
##b=20
##result=add(a,b)
##print(result)




"""
finding EVEN or ODD using function
"""
##def find(a):
##    if a%2==0:
##       print("EVEN")
##    else:
##        print("ODD")
##
##a=2
##find(a)


"""
finding POSITIVE or NEGATIVE or ZERO NUMBER using function
"""
##def num(n):
##    if n==0:
##        return"ZERO NUMBER"
##    elif n>0:
##        return "POSITIVE NUMBER"
##    else:
##        return "NEGATIVE NUMBER"
##
##a=int(input())
##print(num(a))


"""
finding PRIME NUMBER using function
"""
##def prime(z):
##    n=1
##    c=0
##    while n<=z:
##        if z%n==0:
##            c+=1
##        n+=1
##    if c==2:
##        return "PRIME NUMBER"
##    else:
##        return "NOT PRIME NUMBER"
##
##a=int(input())
##print(prime(a))



"""
MULTIPLE TABLES using function
"""
##def multiple(z):
##    for i in range(m,n+1):
##        print (a,"X",i,"=",a*i)
##
##a=int(input())
##m,n=map(int,input().split())
##multiple(a)



"""
REVERSE OF A NUMBER using function
"""
##def reverse(n):
##    result=0
##    while n!=0:
##        r=n%10
##        n=n//10
##        result=result*10+r
##    return result   
##
##a=int(input())
##if a==0:
##    print(a)
##elif a>0:
##    print(reverse(a))
##else:
##    a=abs(a)
##    print(-reverse(a))


"""
COUNTING given numbers
"""
##def count(n):
##    c=0
##    while n!=0:
##        r=n%10
##        n=n//10
##        c+=1
##    return c    
##a=int(input())
##if a>0:
##    print(count(a))
##else:
##    a=abs(a)
##    print(count(a))


"""
NUMBER of EVEN and ODD digits in a given number
"""
##def even_odd_count(n):
##    a=b=0
##    while n:
##        r=n%10
##        n=n//10
##        if r%2==0:
##            a+=1
##        else:
##            b+=1
##    if a%2==0 and b%2==0:
##       return "EVEN"
##    elif a%2==1 and b%2==1:
##       return "ODD"
##    else:
##       return "NOT EVEN AND NOT ODD"
##c=int(input())
##print(even_odd_count(c))
            


"""
LCM of 2 numbers usind function
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
GCD of 2 numbers using function
"""
##def gcd(a,b):
##        while True:
##            if a>b:
##                a,b=b,a
##            b=b%a    
##            if b==0:
##                return a
##                
##       
##a,b=map(int,input().split())
##print(gcd(a,b))
    

"""
GCD of 2 numbers using function in recursion 
"""
##def gcd(a,b):
##    if b==0:
##        return a
##    if a>b:
##        a,b=b,a
##    return gcd(a,b%a)    
##
##a,b=map(int,input().split())
##print(gcd(a,b))



"""
ARMSTRONG NUMBER using function
if 153 --> 1**3 + 5**3 + 3**3 = 153 is a armstong number
"""
##def armstrong(a):
##    c=0
##    while a!=0:
##        r=a%10
##        a=a//10
##        c+=1  
##    s=0
##    b=a
##    while a!=0:
##        r=a%10
##        a=a//10
##        s+=r**c
##    return s
##    if b==s:
##        return "Armstrong Number"
##    else:
##        return "Not Armstrong Number"
##        
##a=int(input())
##print(armstrong(a))


"""
ARMSTRONG NUMBER using function in recurtion
if 153 --> 1**3 + 5**3 + 3**3 = 153 is a armstong number
"""
##def digitcount(num):
##    dc=0
##    while num:
##        num=num//10
##        dc+=1
##    return dc
##def isarmstrong(num,dc):
##    if num==0:
##        return 0
##    return pow(num%10,dc)+isarmstrong(num//10,dc)
##
##num=int(input())
##dc=digitcount(num)
##print(num==isarmstrong(num,dc))

"""
PERFECT NUMBER using function
6 --> has factors of 1,2,3 so add 1+2+3=6 , 6 is perfect number
"""
##def perfect(a):
##    n=1
##    s=0
##    while n<a:
##        if a%n==0:
##            s+=n
##        n+=1
##    if s==a:
##        return ("Perfect Number")
##    else:
##        return("Not Perfect Number")
##        
##b=int(input())
##print(perfect(b))


"""
28 : 1,2,4,7,14
1+2+4+7+14 = 28. so, 28 is a perfect number.
so we use to search half of that number i.e., 14
so, simpllty we use sqrt to reduce recursion.
25 is near to the 28 so, sqrt of 25 is 5 so we can check recursion upto 5
"""
##import math as m
##
##def isperfect(num): # num=28
##    d=int(m.sqrt(num))#d=5
##    res=1
##    for i in range(2,d+1):#(2,6)
##        if num%i==0: #28%2==0 28%3!=0 28%4=0
##            res+=i+num//i # res=2+28//2 --> res=2+14 =16  res=4+28//4 --> 4+7 =11 1+16+11
##    return num==res  28==28       
##num=int(input())
##print(isperfect(num))


"""
COUNTING the given numbers factors
28 --> 1 2 4 7 14 28
So,28 has 6 factors      
"""
##import math as m
##
##def countfactors(num):
##    fc=2
##    a=int(m.sqrt(num))
##    for i in range(2,a+1):
##        if num%i==0:
##            if i==num//i:
##                fc+=1
##            else:
##                fc+=2
##    return fc        
##    
##a=int(input())
##print(countfactors(a))

##import math as m
##
##def countfact(num,a): #(10,3) (10,2) (10,1)
##    if a==1: #a!=3 a!=2 a==1
##        return 2 #2---------------------> 2 
##    if num%a==0: #10%2==0
##        if a==num//a:  #2!=10//2
##            return 1+countfact(num,a-1)
##        else: #2+(10,1)------------------------> 2 #10=2+2=4
##            return 2+countfact(num,a-1)
##    else: #else:
##        return 0+countfact(num,a-1) #(10,2)
##    
##num=int(input()) #10
##a=int(m.sqrt(num)) #3
##print(countfact(num,a))






"""
given number is CIRCULAR PRIME are not
37 --> is prime
73 --> is also prime so,37 is a circular prime
"""
##import math as m
##def countfactors(num,a):
##    if a==1:
##        return 2
##    if num%a==0:
##        if a==num//a:
##            return 1+countfactors(num,a-1)
##        else:
##            return 2+countfactors(num,a-1)
##    else:
##        return 0+countfactors(num,a-1)
##def reverse(num):
##    rev=0
##    while num:
##        r=num%10
##        num=num//10
##        rev=rev*10+r
##    return rev    
##num=int(input())
##a=int(m.sqrt(num))
##if (countfactors(num,a)==2):
##    print("Prime")
##    rev=reverse(num)
##    a=int(m.sqrt(num))
##    if(countfactors(rev,a)==2):
##        print("Circular Prime")
##    else:
##        print("Not A Circular Prime")
##else:
##    print("Not Prime")






"""
MEGA PRIME
37 is Mega Prime because 3 and 7 is also prime.
##"""
##def prime(num):
##    z=0
##    n=1
##    while n<=num:
##        if num%n==0:
##            z+=1
##        n+=1
##    return z
##def individual(num):
##    while num:
##        r=num%10
##        num=num//10
##        print(prime(r))
##a=int(input())
##if (prime(a)==2):
##    print("P")
##    b=individual(a)
##    if (prime(a)==2) and (prime(a)==2):
##        print("MEGA PRIME")
##else:
##    print("NP")
"""
SEMI PRIME
6 is a semiprime number as it is a
product of two prime numbers 2 and 3.
37
"""







"""
LIST[]
TUPLE()
DICTIONARIES{}
"""
"""
LIST
Pre-Defined : Functions: sum,min,max,len
              Methods: append,insert -----> inserting values
                       pop,remove -----> deleting values
"""
##data=[1,2,3,4,5,6,7,8,9,10,100,100]
##print(type(data))
##print(sum(data))
##print(min(data))
##print(max(data))
##print(len(data))
##print(data.count(100)) # count(value)
##data.append(100) # append(value)
##print(data)
##data.insert(2,300) # insert(index position , value)
##print(data)
##data.pop(3) # pop(indexposition)
##print(data)
##data.remove(100) # remove(value)
##print(data)
##data.sort() # sort() ascending order
##print(data)
##data.reverse() # reverse() reverse of list values
##print(data)
####data.sort(reverse==True) # sort(reverse=True) for decending order
####print(data)
##
##a=[1,0,1,0]
##print(any(a))
##a=[0,0,0,0]
##print(any(a))
##a=[1,0,1,0]
##print(all(a))
##a=[1,2,3,4,5]
##print(all(a))



##size=int(input())
##data=list(map(int,input().split()))
##
##print(data)
##
##for i in range(len(data)):
####    print(i,data[i])
##    print(data[i],end=" ")
##
##for i in data:
##    print(i,end=" ")
##    
