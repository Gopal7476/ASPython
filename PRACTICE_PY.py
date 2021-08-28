"""
-------------------->  BASIC <--------------------------
"""
##print("HAI,HELLO WORLD!")
##print("THIS IS PYTHON PROGRAMMING")
##print("HELLO, GOPAL")
##
##a=10
##b=20
##print(a+b)
##
##a=int(input("Enter The 1st Value\t"))
##b=int(input("Enter The 2nd Value\t"))
##print("Addition Of Two Numbers = ",a+b)
##print("Subtraction Of Two Numbers = ",a-b)
##print("Multiplication Of Two Numbers = ",a*b)
##print("Division(Integer) Of Two Numbers = ",a/b)
##print("Division(Float) Of Two Numbers = ",a//b)
##print("Modulo Of Two Numbers = ",a%b)
##a,b=map(int,input("Enter The TWO Values\t").split())
##c=a+b
##print(c)

"""
------------------> CONDITIONAL STATEMENTS <----------------
--> if statement
--> Nested if statement
--> elif statement
--> if & else ststement
"""
"Q)Programming Using if Statement"
##T=int(input("Enter The Value\t"))
##if T%2==0:
##    print(T,"Number Is EVEN")
##
##T=int(input("Enter The Value\t"))
##if T%2==0:
##    print(T,"Number Is EVEN")
##else:
##    print(T,"Number Is ODD")
##
##T=int(input("Enter The Value\t"))
##if T%2==0:
##    print(T,"Number Is EVEN")
##elif T%2!=0:
##    print(T,"Number Is ODD")
##else:
##    print(T,"Number Is EVEN OR ODD")

"Q)Programming To Find The Biggest Number"
##T=int(input("Enter The Value\t"))
##N=int(input("Enter The Value\t"))
##if T<N:
##    print(T,"Is Lessser Than",N)
##elif T>N:
##    print(T,"Is Greater Than",N)
##else:
##    print(T,"Is Equal To",N)


"Q)Eligible For Voting"
##T=int(input("Enter The Value\t"))
##if T>=18:
##    print("Eligible For Voting")
##else:
##    print("Not Eligible For Voting")



"""
--------------> LOOPS <-------------------------
--> for loop
--> while loop
---------------> KEY WORDS <--------------------
>> pass
>> break
>> continue
"""


"Q)Programming Using for Loop"
##a=11
##for i in range(0,a):
##    print(i)
##
##b=0.5
##for i in range(0,11):
##    print(i+b)
##
##a=11
##for i in range(0,a):
##    print(i,end=" ")
##
##b=0.5
##for i in range(0,11):
##    print(i+b,end=" ")

##a=11
##for i in range(0,11):
##    print(i)
##    print(i+0.5)

##T=int(input("Enter The Value\t"))
##for i in range(0,T+1):
##    print(i,end=' ')
##    print(i+0.5)

##a=5
##for i in range(0,a): # 0 1 2 3 4
##    print(i,"i")
##    for j in range(0,i): # - 0 (0,1) (0,1,2) (0,1,2,3)
##        print(j,"j")

##n=10
##for i in range(1,n+1):
##    if i%3!=0:
##        print(i)
##        continue
##        
##               
##n=10
##for i in range(0,n+1):
##    if i!=4:
##        print(i)
##        break
##        
##
##n=10
##for i in range(0,n+1):
##    if i%5!=0:
##         print(i)
##         continue  
       


##n=int(input())
##for i in range(0,n+1):
##    if i%2==0:
##        print(i)
##        pass
##        continue
##        break

"""
-------------> PRINTING PATTERN <---------------
"""

##n=5
##for i in range(1,n):
##    for j in range(0,n):
##        print("#",end="")
##    print()    
##
##n=5
##for i in range(1,n):
##    for j in range(0,n):
##        print("#",end=" ")
##    print()
##
##n=5
##for i in range(1,n):
##    for j in range(0,i):
##        print("#",end='')
##    print()
##
##
##n=5
##for i in range(1,n):
##    for j in range(1,n-i):
##        print(end=' ')
##    for k in range(0,i):
##        print("#",end="")
##    print()    
##
##
##
##n=5
##for i in range(1,n):
##    for j in range(1,n-i):
##        print(end=" ")
##    for k in range(0,i):
##        print("#",end='')
##    for l in range(0,i-1):
##        print("#",end="")
##    print()
##
##
##
##n=5
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or i==n or j==1 or j==n:
##            print("#",end=" ")
##        else:
##            print(" ",end=" ")
##    print()        
        




    
"Q)Programming Using while Loop"
##a=5
##t=0
##while t<=a : # 0<=5 1<=5 2<=5 3<=5 4<=5 5<=5
##    print(t) #   0    1     2    3    4    5
##    t+=1
##
##a=int(input("Enter The Value\t"))
##t=float(input("Enter The Value\t"))
##while t<=a:
##    print(t)
##    t+=1
    


"Q)Programming to finding prime number"
##a=int(input("Enter The Value\t"))
##cnt=0
##for i in range(1,a+1):
##    if a%i==0: 
##            cnt+=1
##if cnt==2:
##        print(a,"Is A PRIME NUMBER")
##else:
##        print(a,"Is NOT A PRIME NUMBER")
##
##
##
##T=int(input("Enter The Number Of TEST CASES\t"))
##for j in range(0,T):
##    a=int(input("Enter The Value\t"))
##    for _ in range(1,a):
##        if a%_==0:
##            cnt+=1
##    if cnt==2:
##        print(a,"is a PRIME NUMBER")
##    else:
##        print(a,"is NOT a PRIME NUMBER")
##
##   
##
##
##T=int(input("Enter The Number Of TEST CASES\t"))
##while T>0:
##    a=int(input("Enter The Value\t"))
##    for _ in range(1,a):
##        if a%_==0:
##            cnt+=1
##    if cnt==2:
##        print(a,"is a PRIME NUMBER")
##    else:
##        print(a,"is NOT a PRIME NUMBER")
##    T-=1


"""
Q)PRIME NUMBERS in the GIVEN RANGE
EX: INPUT : 1 to 5
    OUTPUT : 2,3,5 are primes
"""    
##a,b=map(int,input("Enter The STARTING RANGE and ENDING RANGE\t").split())
##for i in range(a,b+1):
##    cnt=0
##    for j in range(1,i+1):
##        if i%j==0:
##            cnt+=1
##    if cnt==2:
##        print(i,"PRIME NUMBER")
##    else:
##        print(i,"not prime")
    

"""
Q)EVEN and ODD NUMBERS in GIVEN RANGE
EX: INPUT : 1 to 5
    OUTPUT : 1,3,5 are odd numbers
             2,4 are even numbers
"""             
##a,b=map(int,input("Enter The STARTING RANGE and ENDING RANGE\t").split())
##for i in range (a,b+1):
##    if i%2==0:
##        print(i,"Is EVEN NUMBER")
##    else:
##        print(i,"Is ODD NUMBER")


"""
Q)Finding Given Number INDIVIDUAL PRIME NUMBERS
EX: INPUT : 15
    OUTPUT : 1 is prime
             5 is prime
"""     
##n=int(input("Enter The Value\t"))
##while n!=0:
##    cnt=0
##    rem=n%10
##    for i in range(1,rem+1):
##        if rem%i==0:
##            cnt+=1
##    if cnt==2:
##        print(rem,"PRIME")
##    elif rem==1 or rem==0:
##        print(rem,"Either PRIME Or NON PRIME")
##    else:
##        print(rem,"NOT PRIME")
##
##    n=n//10    


"""
Q)Finding Given Number Is a MEGA PRIME OR NOT
EX: INPUT : 17
    OUTPUT : 17 is prime number
              1 is also prime number
              7 is also prime number
             so,17 is a prime number
"""    
##n=int(input("Enter The Number\t"))
##t=n
##a=len(str(n))
##cnt=0
##x=0
##for i in range (1,n+1):
##    if n%i==0:
##        cnt+=1
##if cnt==2:
##    print(n,"prime")
##
##    while n!=0:
##            c=0
##            rem=n%10
##            for j in range (1,rem+1):
##                if rem%j==0:
##                    c+=1
##            if c==2:
##                print(rem,"prime")
##                x+=1
##            n=n//10
##    if x==a:
##        print(t,"is also a mega prime")
##    else:
##        print(t,"not mega prime")
##else:
##    print(n,"not prime")
                


"""
---------------> CORE DATATYPES <----------
--> list
--> set
--> tuple
--> dictnaries
------------> IN-BUILD FUNCTION <-----------
>> len   >> min    >> max
>> sort  >> count  >> index
---------------> KEY WORDS <---------------
>> append             >> pop
>> insert             >> remove
>> extend             >> del
>> union              >> clear
>> update
>> intersection
"""



##a=[14,98,57,24,36,14,6,9,75,20,34,57,57,44,65]
##print("Len",len(a))
##print("Min",min(a))
##print("Max",max(a))
##print("Count Of 57",a.count(57))
##a=sorted(a)
##print("Sort",a)
##a=a.index(9)
##print("Index ",a)
##
##
##
##
##
##b=[1,2,4,5]
##b.append(6)
##print("Append No.6",b)
##b.insert(2,3)
##print("Insert No.3 on Position 2",b)
##b.extend([7])
##print("Extend To No.7",b)
##b.pop()
##print("Pop",b)
##b.remove(6)
##print("Remove",b)
##b.clear()
##print("Clear",b)
##
##
##
##
##
##c=[11,12,13,14,15]
##del(c)
##print("Del")


"Q)Using in-build functions"
##a=[14,98,25,14,76,32,26,25,15,14]
##print(a)
##print("length of a list",len(a))
##print("maximum number in a list",max(a))
##print("minimum number in a list",min(a))
##print("sort",a.sort(),a)
##print("count",a.count(14))
##print("index",a.index(76))


"Q)Using key words"
##a=[1,2,3,4,5]
##a.append(6)
##print("append in a list",a)
##a.insert(5,7)
##print(a)
##a.extend(8)
##print(a)





"Q)CREATING a list"
##a=[22,14,69,75,34]
##for i in range(0,5):
##    print(a[i])
##
##c=[]
##a=int(input("How Many Elements Do U Insert\t"))
##for i in range (a) :
##    b=int(input("enter the element\t"))
##    c.append(b)
##print(c)


##import math
##print(math.sqrt(1234567891234))
##
##
##
##N=int(input())
##s=t=u=v=0
##x=0
##while x>=0: 
##   b=x**2-N
##   if b<0:
##       s=b
##       u=x
##   else:
##       t=b
##       v=x
##   x+=1
##   if s<=-1 and t>0:
##       a=((u+v)/2)
##       print(a)
##       break
##while a:
##    c=((1/2)*(a+(N/a)))
##    d=c
##    if a==c:
##        break
##    print("D",d)
##    a=c
##print("D",d)    
##       
##   
##


"""
DR_PYTHON TEST-1
"""
"""
Patlu and Motu works in a building construction, they have to put some number of bricks N from one place to another,
and started doing their work. They decided , they end up with a fun challenge who will put the last brick.
They to follow a simple rule, In the i'th round, Patlu puts i bricks whereas Motu puts ix2 bricks.
There are only N bricks, you need to help find the challenge result to find who put the last brick.
"""
##N=int(input())
##a=0
##while N!=0:
##    if N!=1:
##        a+=1
##        N=N-a
##        print(a)
##        if N==1 or N<a:
##            print("MOTU")
##            break
##        if N!=1:
##            b=a*2
##            N=N-b
##            if N==1 or N<b:
##                print("PATLU")
##                break



"""
There are three planes A, B and C. Plane A will takeoff on every pth day i.e. p, 2p, 3p and so on.
Plane B will takeoff on every qth day and plane C will takeoff on every rth day.
There is only one runway and the takeoff timing is same for each of the three planes on each day.
Your task is to find out the maximum number of flights that will successfully takeoff in the period of N days.
"""
##T=int(input())
##while T!=0:
##    N,p,q,r=map(int,input().split())
##    d=0
##    for i in range(1,N+1):
##        if(i%p==0) and (i%q!=0) and (i%r!=0):
##            d+=1
##        if (i%p!=0) and (i%q==0) and (i%r!=0):
##            d+=1
##        if(i%p!=0) and (i%q!=0) and (i%r==0):
##            d+=1
##    print(d)        
##    T-=1



"""
Sudha is an intelligent girl and always plays with numbers.
One day she looked at the number and observed a smaller number followed by a larger number and vice versa and named it as a wave number.
Now we need to check whether the given number  N is a wave number or not.
"""
##num=int(input())
##d=num%10
##num=num//10
##while num:
##    r=num%10
##    num=num//10
##    if (d%2==0 and r%2==0) or (d%2==1 and r%2==1):
##        print("Yes")
##        break
##    d=r
##else:
##    print("No")




"""
DR_PYTHON TEST-2
"""

##n=int(input())
##l=[]
##for i in str(n):
##    l.append(int(i))
##s=0
##for i in range(len(l)):
##    print(s)
##    s+=pow(l[i],i+1)
##if s==n:
##    print(n,"Disarium Number")
##else:
##    print(n,"Not A Disarium Number")



##n=int(input())
##c=d=0
##e=f=n
##while n!=0:
##    r=n%10
##    c+=1
##    n=n//10    
##while c!=0:
##    r=e%10
##    d+=pow(r,c)
##    e=e//10
##    c-=1
##if f==d:
##    print(f,"Disarium Number")
##else:
##    print(f,"Not A Disarium Number")


##n=int(input())
##m=int(input())
##d={}
##d[220]=284
##d[1184]=1210
##d[2620]=2924
##d[5020]=5564
##d[6232]=6368
##d[10744]=10856
##d[12285]=14595
##d[17296]=18416
##d[63020]=76083
##d[66928]=66992
##if n in d:
##    if d[n]==m:
##        print("Amicable Numbers")
##    else:
##        print("Not Amicable Numbers")
##else:
##    print("Not Amicable Numbers")




##a,b=map(int,input().split())
##m=n=1
##c=d=0
##while m<=(a//2):
##    if a%m==0:
##        c+=m
##    m+=1    
##while n<=(b//2):
##    if b%n==0:
##        d+=n
##    n+=1    
##if c==b and d==a:
##    print("Amicable Number")
##else:
##    print("Not Amicable Number")



##a=int(input())
##c=e=d=f=0
##while a!=0:
##    rem=a%10
##    c+=1
##    if rem==1:
##        d=c-1
##        if d==0:
##            f=1
##        if d==1:
##            f=2
##        else:
##            print("D",d)
##            e=pow(2,d)
##            print("E",e)
##    f=f+e
##    print("F",f)
##    a=a//10



    
