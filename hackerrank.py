###print hello world
##print("Hello World")






###print even or odd  #3,24,  #5,20,18
##n=int(input())
##if 2<n<=5:
##    if n%2==0:
##        print("Not Weird")
##    else:
##        print("Weird")
##else:
##    if 6<n<20:
##        if n%2==0:
##            print("Weird")
##        else:
##            print("Not Weird")
##    else:
##        if n==20:
##            print("Weird")
##        else:    
##            if n>=20:
##                if n%2==0:
##                    print("Not Weird")
##                else:
##                    print("Weird")




###print sum,difference,multiplication  #3,5
##a=int(input())
##b=int(input())
##c=a+b
##d=a-b
##e=a*b
##print(c)
##print(d)
##print(e)


###print division and float division  #4,3
##a=int(input())
##b=int(input())
##c=a//b
##d=a/b
##print(c)
##print(d)



###print square of the number in given range #3 -->0 1 2-->0 1 4
##n=int(input())
##for i in range(0,n):
##    print(i*i)


###print numbers in sequence #3 --->123  #10-->12345678910
##n=int(input())
##for i in range(1,n+1):
##     print(i,end='')      
##
##
##
##n=int(input())
##w=1
##while w<=n:
##    print(w,end="")
##    w+=1




##def is_leap(year):
##    if year%4!=0:
##        leap=False
##        return leap
##    elif year==2100:
##        leap=False
##        return leap
##    else:
##        leap=True
##        return leap
##year=int(input())
##print(is_leap(year))



###factorial of number (HE)
##N=int(input())
##fact=1
##while N>0:
##    temp=N
##    N-=1
##    fact=temp*fact
##print(fact)
## 
##     
##n=int(input()) # 5
##fact=1
##for i in range(1,n+1): # (1,6)
##    fact*=i  # 1*1*2*3*4*5
##print(fact)





##a=[]
##n=int(input("Enter How Many Elements U Want?\t"))
##for i in range (n):
##    a.append(int(input()))
##    a.sort()
##print(a)








##T=int(input())
##N=int(input())
##K=int(input())
##temp=0
##for t in range(0,T):
##    a=[]
##    for i in range(0,N):
##        b=int(input())
##        a.append(b)
##        
##    for _ in range (0,K):
####            temp=a[4]
####            a[4]=a[3]
####            a[3]=a[2]
####            a[2]=a[1]
####            a[1]=a[0]
####            a[0]=temp
##    print(a)  
##
##T=int(input())
##N=int(input())
##K=int(input())
##for t in range(0,T):
##    a=[]
##    for i in range(0,N):
##        b=int(input())
##        a.append(b)
##    print(a)
##    for _ in range(0,K):
##            a=a[-1:] + a[:-1]
##    ##    a.insert(0,a.pop())
##    print(a)  












##a=int(input())
##b=int(input())
##c=int(input())
##a,b=b,a
##d=a*c
##e=c+b
##print(d,e)



##a=int(input())
##b=int(input())
##c=a//b
##d=a%b
##print(c)
##print(d)
##e=(c,d)
##print(e)



##a=3
##b=4
##c=5
##print(pow(a,b))
##print(pow(a,b,c))


##a=int(input())
##b=int(input())
##c=int(input())
##d=int(input())
##print(pow(a,b)+pow(c,d))


##a=int(input())
##for i in range(1,a):
##    for j in range(0,i):
##        print(i,end="")
##    print()
##
##for i in range(1,int(input())):
##    print(int(i*10**i//9))
    
    
    
##n=int(input())
##a=[]
##for i in range(0,n):
##    b=int(input())
##    a.append(b)
##print(a)
##a.sort()
##print(a)
##print(max(a))





##n = int(input())
##a=[]
##d=[]
##for i in range(n):
##    b=int(input())
##    a.append(b)
##c=sorted(a)
##if c[-2]<c[-1]:
##    print(c[-2])
##else:
##    if c[-2]==c[-1]:
##        if c[-3]<c[-2]:
##            print(c[-3])



##if __name__ == '__main__':
##    n = int(input())
##    arr = map(int, input().split())
##    arr=set(arr)
##    arr=list(arr)
##    arr=sorted(arr)
##    print(arr[-2])
        


"""
leetcode-9
Palindrome Number
"""
##n=int(input(""))
##b=n
##a=0
##if n>=0:
##    while n!=0:
##        m=n%10
##        n=n//10
##        a=a*10+m
##    if b==a :
##        print(True)
##    else:
##        print(False)
##
##else:
##    print(False)



"""
leetcode-5
Reverse Number
"""
##n=int(input(""))
##b=n
##a=0
##
##if n>=0:
##    while n!=0:
##        m=n%10
##        n=n//10
##        a=a*10+m
##    if ((-2**31)<=a<=((2**31)-1)):    
##        print(a)
##    else:
##        print(0)
##else:
##    c=-n
##    while c!=0:
##        m=c%10
##        c=c//10
##        a=a*10+m
##    if ((-2**31)<=n<=((2**31)-1)):    
##        print(-a)
##    else:
##        print(0)
    
    
"""
HackerRank
List Comprehensions
"""
##a=int(input(""))
##b=int(input(""))
##c=int(input(""))
##d=int(input(""))
##for i in range(0,a+1):
##    for j in range(0,b+1):
##        for k in range(0,c+1):
##            e=i+j+k
##            if e!=d:
##                print([i,j,k],end=" ")



"""
HackerEarth
"""
##T=int(input())
##for i in range(T):
##    n=int(input(""))
##    if n<=5:
##        n=1
##        print(n)
##    else:
##        if n>5:
##            c=n//5
##            d=c*5
##            a=n-d
##            if 1<=a<=5:
##                a=1
##            elif a==0:
##                print(c)
##            else:
##                a=a-5        
##            print(a+c)
        
   

##n=int(input())
##s=result=0
##p=1
##while n!=0:
##    r=n%10
##    s+=r
##    p*=r
##    n=n//10
##
##result=p-s
##print(p,s)
##print(result)


##L=int(input())
##N=int(input())
##for i in range(0,N+1):
##    W,H=map(int,input().split())
##    if W<L or H<L:
##        print("UPLOAD ANOTHER")
##    elif W==H:
##        print("ACCEPTED")    
##    elif W>L and H>L:
##        if W==L:
##            print("ACCEPTED")
##        else:
##            print("CROP IT")
##    else:
##        print("CROP IT")
##                


##N=int(input())
##a=list(map(int,input().split()))
##answer=1
##print(len(a))
##for i in range(len(a)):
##    answer=answer*a[i]
##print(answer)    
    


            

##x=int(input())
##y=int(input())
##z=int(input())
##n=int(input())
##print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n])





##a=int(input())
##for i in range(1,a+1):
##    for j in range(i,a):
##        print(i)


##import calendar
##m, d, y = map(int, input().split())
##print(calendar.day_name[calendar.weekday(y, m, d)].upper())


##n, m = input().split()
##arr = [int(x) for x in input().split()]
##A = set([int(y) for y in input().split()])
##B = set([int(z) for z in input().split()])
##count = [0 + 1 if x in A else 0-1 if x in B else 0 + 0 for x in arr]
##print(sum(count))
    

##k,m=map(int,input().split())
##n = (int(x) for x in input(k).split())
##
##print(n)


##def getKey(x):
##    if x.islower():
##        return(1,x)
##    elif x.isupper():
##        return(2,x)
##    elif x.isdigit() :
##        if int(x)%2==1:
##            return(3,x)
##        else :
##            return(4,x)
##
##print(*sorted(input(),key=getKey),sep='')



##ui = input().split()
##x = int(ui[0])
##print(eval(input()) == int(ui[1]))


##n=int(input())
##d=0
##for i in range(2,n):
##    c=0
##    for j in range(1,i+1):
##        if i%j==0:
##            c+=1
##    if c==2:
##        print(i)
##        d+=1
##
##print("D",d)


n=int(input())
a=1
b=n//2
c=0
while a<b+1:
    if n%a==0:
        print(a)
        c+=a
    a+=1
if c==n:
    print(c,n)
    
    
    
