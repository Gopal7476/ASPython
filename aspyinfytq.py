##n=int(input())
##for i in range(n):
##    for j in range(0,i+1):
##        print("*" , end=' ')
##    print()


###prime program for multiple number
##t=int(input())
##while(t):
##        n=int(input())
##        c=0
##        for i in range(1,n+1):
##            if n%i==0:
##                c+=1
##        t-=1        
##        if c==2:
##            print(n,"it is a prime")
##        else:
##            print(n,"it is not prime")
##
##
##
###prime program for single number
##n=int(input())
##flag=0
##for i in range(2,n):
##    if(n%i==0):
##        flag=1
##        break
##if flag==1:
##    print("not prime")
##else:
##    print("prime")
##
##
##
##
##n=int(input())
##flag=0
##for i in range(2,n//2):
##    if(n%i==0):
##        flag=1
##        break
##if flag==1:
##    print("not prime")
##else:
##    print("prime")
##
##
##
##n=int(input())
##flag=0
##import math
##x=int(math.sqrt(n))
##for i in range(2,x+1):
##    if(n%i==0):
##        flag=1
##        break
##if flag==1:
##    print("not prime")
##else:
##    print("prime")
##
##
##
##
##
##n=int(input())
##flag=0
##i=2
##while(i*i<=n):
##    if(n%i==0):
##        flag=1
##    i+=1   
##if flag==1:
##    print("not prime")
##else:
##    print("prime")




##N=25
##seive=[1 for i in range(N+1)]
##print(seive)



##N=int(input())
##seive=[1]*(N+1)
##seive[0]=0
##seive[1]=0
##i=2
##while(i*i<=N):  #2*2=4<=25  true
##    if seive[i]==1:    #seive[2]==1   true
##        for j in range(i*i,N+1,i):
##            seive[j]=0
##    i+=1        
##x=int(input())
##if seive[x]==1:
##    print("prime")
##else:
##    print("not prime")
##print(seive)




##n=int(input())
##c=0
##for i in range(1,n+1):
##    if n%i==0:
##        c+=1
##if c==2:
##     print("prime")
##else:
##     print("not prime")



##s=int(input())
##e=int(input()) 
##while s<=e:
##    cnt=0
##    for i in range(1,s+1):
##        if s%i==0:
##            cnt+=1
##    if cnt==2:
##        print(s,"prime")
##    s+=1              
       



##n=int(input())
##for j in range(2,n+1):
##    cnt=0
##    for i in range(1,j+1):
##        if j%i==0:
##            cnt+=1
##    if cnt==2:
##        print(j,"prime")
##    else:
##        print(j,"not prime")




        
 

##n=int(input())  #5
##x=2
##z=0
##while x<=n:    #2<=5     3<=5    4<=5    5<=5   6!<=5
##    c=0
##    for i in range(1,x+1):  #(1,3)     (1,4)    (1,5)    (1,6)
##        if x%i==0:  #2%1==0    2%2==0 ;  3%1==0  3%2==0  3%3==0 ;  4%1==0  4%2==0  4%3==0   4%4==0 ; 5%1==0   5%2!=0  5%3!=0  5%4!=0   5%5==0
##            c+=1    #2      3      4      5    
##    if c==2:
##        z+=x        #2+3+4+5
##        print(x,"prime")  #2  3   4  5
##    x+=1    #3  4  5  6
##print(z) #






##def is_prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    return True
##print(is_prime(6))
       
            



##def is_prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    return True
##t=int(input())
##for _ in range(t):
##    l,r=map(int,input().split())
##    sum1=0
##    for i in range(l,r+1):
##            if is_prime(i):
##                 sum1+=i
##    print(sum1)    
            
            
            



##
##n=100001
##seive=[1]*n
##def seive_gen():
##    seive[0]=0
##    seive[1]=0
##    i=2
##    while(i*i<=n):
##        if seive[i]==1:
##            for j in range(i*i,n,i):
##                seive[j]=0
##        i+=1        
##t=int(input())
##for _ in range(t):
##    seive_gen()
##    l,r=map(int,input().split())
##    sum1=0
##    for i in range(l,r+1):
##            if seive[i]==1:
##                 sum1+=i
##    print(sum1)





##n=100001
##seive=[1]*n
##prefixsum=[0]*n
##def seive_gen():
##    seive[0]=0
##    seive[1]=0
##    i=2
##    while(i*i<=n):
##        if seive[i]==1:
##            for j in range(i*i,n,i):
##                seive[j]=0    
##        i+=1
##    for i in range(2,n):
##        if seive[i]==1:
##            prefixsum[i]=prefixsum[i-1]+i
##        else:
##            prefixsum[i]=prefixsum[i-1]
##
##t=int(input())
##seive_gen()
##for _ in range(t):
##     l,r=map(int,input().split())
##     print(prefixsum[r]-prefixsum[l-1])







##n=10000001
##seive=[1]*n
##def seive_gen():
##    seive[0]=0
##    seive[1]=0
##    i=2
##    while(i*i<=n):
##        if seive[i]==1:
##            for j in range(i*i,n,i):
##                seive[j]=0    
##        i+=1
##seive_gen()
##t=int(input())
##for _ in range(t):
##    count=0
##    x=int(input())
##    for i in range(x+1):
##        if seive[i]==1:
##            count+=1
##    print(count)





###factors of a number
##
##n=int(input())
##for i in range(1,int(n**0.5)+1):
##    print(end='')
##    if n%i==0:
##        if n//1!=i:
##            print(n//i)
##    
##
##
##
##

##n=25
##seive=[i for i in range(n+1)]  #create a seive with corresponding number given
##def gen_modifiedseive():
##    for i in range(2,int(n**0.5)+1):
##        if seive[i]==i:
##            for j in range(i*i,n+1,i):
##                if seive[j]==j:
##                    seive[j]=i
##    print(seive)
##gen_modifiedseive()
##n=20
##while(n!=1):
##    print(seive[n],end=' ')
##    n=n//seive[n]



##n=11
##seive=[i for i in range(n+1)]  #create a seive with corresponding number given
##def gen_modifiedseive():
##    for i in range(2,int(n**0.5)+1):
##        if seive[i]==i:
##            for j in range(i*i,n+1,i):
##                if seive[j]==j:
##                    seive[j]=i
##    print(seive)
##print(gen_modifiedseive())    
##gen_modifiedseive()
##d={}
##n=10
##while(n!=1):
##   if seive[n] in d:
##       d[seive[n]]+=1
##   else:
##       d[seive[n]]=1
##   n=n//seive[n]    
##print(d)
##ans=1
##for i in d.values():
##    ans*=i+1
##print(ans)








##n=int(input())
##seive=[i for i in range(n+1)]
##print(seive)
##for i in range(2,int(n**0.5)+1):
##    if seive[i]==i:
##        for j in range(i*i,n+1,i):
##           seive[j]=0
##print(seive)                





##
##class solution:
##    def countprimes(self,n:int) -> int:
##        def isprime(x):
##            for i in range(2,int(x**0.5)+1):
##                if x%i==0:
##                    return False
##                return True
##            c=0
##            for i in range(2,n):
##                if isprime(i):
##                    c+=1
##                    return c
##         print(isprime(10))        
##     print(countprimes(10))   
##



### binary search
##def binary_search(arr,low,high,k):
##    mid=(low+high)//2
##    if arr[mid]==k:
##        return True
##    elif arr[mid]>k:
##        return binary_search(arr,0,mid-1)
##    else:
##        return binary_search(arr,mid+1,high)
##    
##
##n=6
##arr=[10,20,15,60,12,14]
##arr.sort()
##k=14
##print(binary_search(arr,0,n-1,k))





### matrix diagonal 1,5,9,3,7 sum=25 
##r=int(input())
##c=int(input())
##mat=[]
##print("Enter the values")
##for i in range(r):
##    a=[]
##    for j in range(c):
##        a.append(int(input()))
##    mat.append(a)             
##for i in range(r):
##        for j in range(c):
##                 print(mat[i][j],end=' ')
##        print()         
##j=len(mat)-1
##pd=0
##sd=0
##for i in range(len(mat)):
##    pd+=mat[i][i]
##    if i!=j:
##        sd+=mat[i][j]
##    j-=1    
##print(pd+sd)




##s="infytq@248"
##s='12345'
##a=[]
##for i in s.split():
##       if i.isdigit():
##           a.append(int(i))
##           
##print(a)

##s="infytq@248"
##i=[int(a) for a in s.split() if a.isdigit()]
####for a in s.split():
####    if a.isdigit():
####        i.append(int(a))
##print(i)
##
##a_string='14ght45'
##numbers=[]
##for word in a_string.split():
##    if word.isdigit():
##        numbers.append(int(word))
##print(numbers)        





##def split():
##    for i in s.split():
##        if i.isdigit():
##               print(i)
##
##s="12345dfe"
##split()
##print(s.isdigit())





"""
INFYTQ FINAL ROUND
"""


##a=5
##s=bin(a)
##print(bin(a))
##print(s.count('1'))
##
##a=5
##b=1
##c=0
##for i in range(a):
##    if a&b==1:
##        c+=1
##    a=a>>1 #shifting operator 
##print(c)

"Q)Reverse of array"
##a=[1,2,3,4,5]
##a.reverse()
##print(a)
##
##a=[1,2,3,4,5]
##print(a[::-1])
##a=[]
##T=int(input())
##for i in range(T):
##    b=int(input())
##    a.append(b)
##print(a)

"Q)Finding MAXIMUM and MINIMUM element in array"
##a=[1,5,6,2,3]
##print(max(a))
##print(min(a))
##
##a=[1,5,6,2,3]
##m=a[0]
##for i in a: 
##    if m<i:
##        print("m>i",m,"<",i)
##        m=i 
##print(m)
##        
##a=[5,6,2,3,1]
##m=a[0]
##for i in a:
##    if m>i:
##        print("m>i",m,">",i)
##        m=i
##print(m)        


"Q)Finding Kth MAXIMUM and MINIMUM element of an array"
##a=[14,15,7,36,76,42,104,1]
##k=int(input())
##a=sorted(a)
##print(a)
##print(a[k-1])
##print(a[-k])

"Q)sort the array without using sorting function"
##a=[0,1,2,1,0]
##for i in range(len(a)):
##    for j in range(i+1,len(a)):
##        if a[i]>a[j]:
##            a[i],a[j]=a[j],a[i]
##print (a)            






##a=list(map(int,input().split()))
##k=int(input())
##for i in range(0,k):
##    x=a.pop()
##    a.insert(0,x)
##print(a)
##
##a=list(map(int,input().split()))
##k=int(input())
##for i in range(0,k):
##   a.insert(0,a.pop())
##print(a)





##x=int(input())
##y=int(input())
##z=int(input())
##five_need=0
##one_need=0
##while (z>0):
##        if (z>5 and x>1):
##            z=z-5
##            x-=1
##            five_need+=1
##        elif (y>z and y>=1):
##                z=z-1
##                y-=1
##                one_need+=1
##        else:
##            break
##        
##if(z==0):
##      print("one",one_need)
##      print("five",five_need)
##else:
##      print("-1")





"Q)no.of words of a string"
##s=input()
##print(len(s.split()))

"Q)no.of words of a string(camelcase)"
##s=input()
##c=0
##for i in s:
##    if i==i.upper():
##        c+=1
##print(c)        





##s=input()
##l=s.split()
##print(len(''.join(l)))



##string = input()
##l = ['a','e','i','o','u','A','E','I','O','U']
## 
##c = 0
##for i in string:
##    if i in l:
##        c+=1
##        l.remove(i)
##print(c)





##s1=input()
##s2=input()
##res=''
##for i in (s1):
##if i in s2:
##res+=i
##print(len(res),res,min(res),max(res))



##s=input()
##if s[::-1]==s:
##    print("yes")
##else:
##    print("no")

"Q)length of the each string"
##s=input()
##t=s.split()
##for i in t:
##    print(len(i))

##s=input()
##t=s.split()
##pos=0
##for i in t:
##    print(len(i),max(i))
    



##n=int(input())
##arr=[]
##for k in range(0,n):
##    b=int(input())
##    arr.append(b)
##profit=[0]*n
##profit[0]=arr[0]
##for j in range(1,n):
##    for i in range(0,j):
##        if arr[j]%arr[i]==0:
##            profit[j]=max(profit[j],profit[i]+arr[j])
##print(profit)
##print(max(profit))


"2 3 1 1 2 4 2 0 1 1"




##mat=[[0 for i in range(4)] for j in range(4)]
##print(mat)
##
##for row in range(4):
##    for col in range(4):
##        print(mat[row][col],end=' ')
##    print()

##matA=[[1,2,3],[4,5,6],[7,8,9]]
##matB=[[9,8,7],[6,5,4],[3,2,1]]
##matC=[[0 for i in range(3)]for j in range(3)]
##for row in range(3):
##    for col in range(3):
##        matC[row][col]=matA[row][col]+matB[row][col]
##        print(matC[row][col],end=' ')
##    print()
##print(matC)


##matA=[[1,2,3],[4,5,6],[7,8,9]]
##matC=[[0 for i in range(3)]for j in range(3)]
##for row in range(3):
##    for col in range(3):
##        matC[row][col]=matA[col][row]
##        print(matC[row][col],end=" ")
##    print()    
##print(matC)        


##matA=[[1,2,3],[4,5,6]]
##matC=[[0 for i in range(3)]for j in range(2)]
##for row in range(3):
##    for col in range(2):
##        matC[row][col]=matA[col][row]
##        print(matC[row][col],end=" ")
##    print()    
##print(matC)        


##matrix=[[1,2,3],
##        [4,5,6]]            
##n=len(matrix)
##m=len(matrix[0])
##row=[0 for i in range(n)]
##col=[1 for j in range(m)]
##print(row)
##print(col)

"""
LEET CODE
"""

##matrix=[[1,2],[4,5]]
##n=len(matrix)
##m=len(matrix[0])
##mat=[[0 for i in range (n)]for j in range(m)]
##for i in range(n):
##    for j in range(m):
##            mat[j][i]=matrix[i][j]
##            
##print(mat)  



##matrix=[[1,2,3],[4,5,6],[7,8,9]]
##n=len(matrix)
##m=len(matrix[0])
##c=0
##for i in range(n):
##    for j in range(m):
##        if matrix[i]==matrix[j]:
##            c+=matrix[i][j]
##            print(c)
##        else:
##            if j==m-(i+1) and i!=j:
##                c+=matrix[i][j]
                         



##mat=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
##primary=0
##secondary=0
##n=len(mat)
##m=len(mat[0])
##for i in range(0,n):
##    for j in range(0,m):
##        if (i==j):
##            primary+=mat[i][j]
##        if ((i+j)==(n-1)) and i!=j:
##             secondary+=mat[i][j]
##print(primary+secondary)



##mat=[[1,1,1],[1,0,1],[1,1,1]]
####mat=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
##n=len(mat)
##m=len(mat[0])
##print(n,m)
##k=[[1 for i in range(m)]for j in range(n)]
##print(k)
##for i in range(n):
##    for j in range(m):
##        if mat[i][j]==0:
##            k[i][j]=mat[i][j]
##            for a in range(0,i):
##                for b in range(0,j):
##                    k[i][j-1]=k[i][j+1]=0
##                    k[i-1][j]=k[i+1][j]=0
##print(k)            
            

####nums=[2,7,11,15]
####target=9
####nums=[3,2,4]
####target=6
####nums=[3,3]
####target=6
##a=len(nums)
##for j in range(0,a):
##    for i in range(0,j):
##        if ((nums[i]+nums[j])==target):
##            print([i,j])
        




##def find_leap_years(given_year):
##    c=0
##    list_of_leap_years=[]
##    while(c<15):
##        if ((given_year%4)==0 or ((given_year%400==0) and (given_year%100==0))):
##                list_of_leap_years.append(given_year)
##                c+=1 
##        given_year+=1        
##               
##        
##
##    return list_of_leap_years
##
##list_of_leap_years=find_leap_years(1784)
##print(list_of_leap_years)


##def create_largest_number(number_list):
##    number_list.sort()
##    res = ""
##    for num in number_list:
##        res = str(num) + res
##
##    return (int(res))
##        
##
##number_list=[87,66,11]
##largest_number=create_largest_number(number_list)
##print(largest_number)







