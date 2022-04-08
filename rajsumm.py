##a=20
##b=30
##print(a+b)
##
##
##x=2
##x+3
##print(x)
##
##
##
##a=110
##b=20
##print(a+b)
##
###-------------------------------------------> Conditional operators (if,elif,else) <----------------------------------------------------
##
###if condition programs
##a=int(input("enter the number\t"))
##if a>=10:
## print(a,"it is bigger")
##print(a)
##
##
##
###if-else condition programs
##a=int(input("enter the number\t"))
##if a<=10:
##    print(a,"is small")
##else:
##    print(a,"is big")
##
##
##
###Q)which number is bigger
##a=int(input("enter the number\t"))
##b=int(input("enter the number\t"))
##if a>b:
##      print(a,"is bigger")
##else:
##      print(b,"is bigger")
##
##
##
##
##
###Q)checking for loging
##accno="12345678910"
##pinno="12345"
##
##acc=input("enter the account number\t")
##pin=input("enter the pin number\t")
##if accno==acc and pinno==pin:
##    print("procced")
##else:
##    print("wrong acc no or pin no")
##
##
##
##
##
##accno="12345678910"
##pinno="12345"
##
##acc=input("enter the account number\t")
##pin=input("enter the pin number\t")
##if accno==acc and pinno==pin: 
##    print("procced")
##elif accno!=acc and pinno!=pin:
##     print("wrong acc no and wrong pin no")    
##     print("please check")    
##elif accno!=acc :  
##    print("wrong acc no")
##    print("please check")
##elif  pinno!=pin:
##    print("wrong pin no")
##    print("please check")
##
##
###Q)eligible for voting
##age=int(input("enter your age\t"))
##if age>=18:
##    print("you are eligible for voting")
##else:
##    print("you are not eligible for voting")
##
##
##
##
###Q)which number is big
##a=int(input("enter the number\t"))
##b=int(input("enter the number\t"))
##if a>b:
##    print(a,"is big")
##elif a==b:
##    print(a,b,"both are equal")
##else:
##    print(b,"is big")
##
##
##
##
##
##
###Q)given number is even or odd
##a=9
##r=a%2
##if r==0:
##    print("even")
##    if r==1:
##        print("odd")
##else:
##    print("not even or odd")
##
##
##
##n=int(input("enter the number\t"))    
##if n%2==0:
##    print(n,"is even")
##else:
##    print(n,"is odd")
##
##
##
##n=int(input("enter the number\t"))
##if n%2==1:
##    print(n,"is odd")
##else:
##    print(n,"is even")
##
##
##
##
##
##
##
##
###Q)eligibility
##per=int(input("enter the percentage\t"))
##bl=int(input("enter the backlog\t"))
##ge=input("enter the gender\t")
##if (per>=75 and bl==0) or ge=='male':
##    print("eligible")
##else:
##    print("not eligible")
##
##
##
##
##per=float(input("enter the percentage\t"))    
##bl=int(input("enter the backlog\t"))
##gen=input("enter the gender\t")
##if gen=="male":
##    print("eligible")
##else:
##    if per>=75 and bl==0:
##        print("eligible")
##    else:
##        print("not eligible")
##
##
##
##
###Q)grading
##marks=float(input("enter the marks\t"))
##if marks>=80:
##    print("A grade")
##elif marks>=60 and marks<80:
##    print("B grade")
##elif marks>=40 and marks<60:
##    print("C grade")
##else:
##    print("failed")
##
##
##
##
##
##
###-------------------------------------------------> Loops (for,while) <--------------------------------------------------------------
##
##for i in range(0,5):
##    print(i)
##    print(i,end=" ")
##
##cnt=0.5
##for i in range(0,11):
##    print(i+cnt,end="   ")
##
##
##
##for i in range (1,11,1):
##    print(i)
##
##
##for i in range(1,101):
##    print(2*i)
##
##for i in range(1,101):
##    print(i,2*i)
##    
##    
##for i in range(1,101):
##    print(i,"*",2,"=",2*i)
##
##
##
##
##
##for i in range(1,11):
##    print(i)
##    if i==5:
##        break
##print("selection done")
##
##
##
##
##
##for i in range(1,11):
##    print(i)
##    if i==5:
##        continue
##print("selection done")
##
##
##
##for i in range(1,11):
##    print(i)
##    if i==5:
##        pass
##print("selection done")
##
##
##
##for i in range (1,21):
##    if i%5==0:
##        print(i)
##        break
##
##
##for i in range (1,21):
##    if i%5==0:
##        print(i)
##        continue
##
##        
##
##for i in range (1,21):
##    if i%5==0:
##        print(i)
##        pass
##
##
##
##
##number=input("enter the number\t")
##b= int(input("enter the number\t"))
##for i in range(1,50):
##    print(i,"*",b,'=',i*b)


##for i in range(1,51):
##    print(i,"*",i,"=",i*i)
##
##
##
##
##number=input("enter the number\t")
##for i in range(1,11):
##    print(i,"*",2,"=",2*i)
##
##
##
##
###Q)reverse of a number
##n=int(input("enter the number\t"))
##res=0
##while n!=0: 
##    rem=n%10 
##    n=n//10
##    res=res*10+rem
##print(res)
##
##
##
###Q)prime number
##n=int(input("enter the number\t"))
##cnt=0
##for i in range(1,n+1):
##    if n%i==0:
##     cnt+=1
##if cnt==2:
##    print(n,"is prime")
##else:
##    print(n,"is not prime")
##
##
##n=int(input("enter the number\t"))
##for i in range(2,n):
##    if n%i==0:
##        print(n,"not prime")
##        break
##else:
##        print(n,"prime")
##
##
##
###Q)mailid and password
##imid='gopal@crick.com'
##ipwd='2020'
##for i in range(4):
##    mid=input("enter the mail id:\t")
##    pwd=input("enter the password:\t")    
##    if imid==mid and ipwd==pwd:
##        print("login sucessful")
##        break
##    else:
##        print("wrong mail id or password")
##else:
##    print("blocked for 24 hours")
##
##
##
##
##av=10
##x=int(input("how many candies you want\t"))
##i=1
##while i<=x:
##    if i>av:
##        break
##    print("candy")
##    i+=1
##print("bye")    
##  
##
##
##for i in range(1,20):
##    if i%3==0 :
##        continue
##    print(i)
##print("bye")    
##
##
##
##for i in range(1,20):
##    if i%3==0:
##        break
##    print(i)
##print("bye") 
##
##
##
##for i in range(1,20):
##    if i%3==0 :
##       pass
##    print(i)
##print("bye") 
##
##
##
##for i in range (1,10):
##    if i%2!=0:
##       pass
##    else:
##        print(i)
##
##
##
##for i in range (1,10):
##    if i%3!=0:
##       pass
##    else:
##        print(i)
##
##
##
###Q)prime numbers in the ginven range
##m=int(input("enter the starting number\t"))
##n=int(input("enter the ending number\t"))
##for j in range(m,n+1):
##    cnt=0
##    for i in range(1,j+1):
##        if j%i==0:
##            cnt+=1
##    if cnt==2:
##        print(j,"is prime")        
##
##
##            
##
###Q)individual prime numbers
##n=int(input("enter the number"))
##while n!=0:
##    c=0
##    rem=n%10
##    for i in range(1,rem+1):
##        if rem%i==0:
##           c+=1
##    if c==2:
##        print(rem)
##    n=n//10    
##
##
##
####Q)mega prime
##n=int(input("enter a number"))
##a=len(str(n))
##cnt=0
##x=0
##for i in range(1,n+1):
##    if n%i==0:
##        cnt+=1
##if cnt==2:
##    print(n,"prime")
##    while n!=0:
##        c=0
##
##        rem=n%10
##        for i in range(1,rem+1):
##             if rem%i==0:
##                c+=1
##        if cnt==2:
##            print(rem,"prime")
##            x+=1
##        n=n//10
##    if x==a: 
##           print("mega prime as well")
##    else:
##           print("not mega prime")
##else:
##    print("not a prime")
    




###-------------------------------------------------> Lists,Set,Tuple,Dictnary <----------------------------------------------------------------------
###
###Q) print the list elements
##a=[2,5,8,7,9]
##for i in range(0,4):
##    print(a[i])
##    
##
##
##a=[5,8,7,5,78,545]
##for i in range(0,4):
##    print('index:',i,'value:',a[i])
##
##
##
##
##a=[5,8,7,5,78,545]
##for i in range(0,len(a)):
##    print('index:',i,'value:',a[i])




##a=[1,23,45,67,89,10]
##for i in a:
##    print(i)
##for i in range(len(a)):
##    print(i,a[i])


    

###Q)length of list
##a=[1,2,5,4,5,8]
##cnt=0
##for i in a:
##    cnt+=1
##print(cnt)    



##a=[1,2,5,4,8,7,6]
##for i in a:
##    print(i,'*',2,'=',2*i)
##
##
##a=[1,2,3,4,5]
##b=int(input("enter the number"))      
##for i in a:
##      print(i,'*',b,"=",b*i)



##a=[1,4,5,5,666,4,7,42,5,4,1,6,9,447,4,5,8]
##a.sort()
##print(a)


###Q)maximum of list
##a=[1,4,6,8,6,23,5,54,147]
##m=a[0]
##for i in a:
##    print("i",i)
##    if m<i:
##        print("i",i)
##        print("m",m)
##        m=i
##        print("i",i)
##        print("m",m)
##print("maximum of list",m)




###Q)minimum of list
##a=[57,2,5,1,4,88,44,6,52]
##m=a[0]
##print(m)
##for i in a:
##    print(i)
##    if m>i:
##        print(m)
##        print(i)
##        m=i
##        print(m)
##print("minimum of list",m)





###Q)enter the list
##a=[]
##print(a)
##b=int(input("enter the elements\t"))
##a.append(b)
##print(a)
##
##
#Q)enter the list
##a=[]
##print(a)
##for i in range(6):
##      b=int(input("enter the number\t"))
##      a.append(b)      
##print(a)





###Q)sorting the list elements
##a=[]
##for i in range (5):
##    b= int(input("enter the elements\t"))
##    a.append(b)
##    a.sort()    
##print(a)





    
###Q)sorting list elements before and after
##a=[]
##c=int(input("enter the range in list\t"))
##for i in range(c):
##    b=int (input("enter the list elements\t"))
##    a.append(b)
##print("before sorting",a)
##a.sort()
##print("after sorting",a)





##a=[]
##for i in range(3):
##    b=int(input("enter the elements"))
##    a.append(b)
##print(a)
##m=int(input("enter the element to search"))
##c=0
##for i in a:
##    if i==m:
##        c+=1
##print(m,'occured',c,"times")        




##a=[]
##c=int(input("enter the range of list\t"))
##for i in range(c):
##    b=int(input("enter the list elements\t"))
##    a.append(b)
##print(a)    
##d=int(input("enter the range of search list\t"))    
##for i in range(d):    
##  m=int(input("enter the element to search\t"))    
##  c=0
##  for i in a:
##    if i==m:
##      c+=1
##  print(m,"occured",c,"times")







###Q)prime numbers in the list
##a=[]
##for i in range(5):
##    b=int(input("enter elements"))
##    a.append(b)
##print(a)
##for i in a:
##    c=0
##    for j in range(1,i+1):
##        if i%j==0:
##            c+=1
##    if c==2:
##            print(i,"prime")
##
##
##
##
##a=[]
##c=int(input("enter the range\t"))
##for i in range(c):
##    b=int(input("enter elements"))
##    a.append(b)
##print(a)
##for i in a:
##    c=0
##    for j in range(1,i+1):
##        if i%j==0:
##            c+=1
##    if c==2:
##            print(i,"prime")





###Q)maximum length of a list element
##a=["apple","strawberry","pineapple"]
##m=len(a[0])
##for i in a:
##    if len(i)>m:
##        m=len(i)
##print(m)        




##a=['apple','strawberry','pineapple']
##m=len(a[0])
##name=a[0]
##for i in a:
##    if len(i)>m:
##        m=len(i)
##        name=i
##print(m,"is length of",name)        



##a=[]
##for i in range(3):
##    b=input("enter the list")
##    a.append(b)
##print(a)    
##m=len(a[0])
##name=a[0]
##for i in a:
##    if len(i)>m:
##        m=len(i)
##        name=i
##print(m,"is length of",name)




##a=(4,5,5,6,2,7)
##for i in a:
##    print(i)
##    



##a=[74,5,87,9,47,69]
##b=[2,57,65,14,9,47]
##for i in b:
##    for j in a:
##        if i not in a:
##            a.append(i)
##print(a)





##a=[]
##b=[]
##for i in range(3):
##    a.append(int(input("enter the elements")))
##for j in range(3):
##    b.append(int(input("enter the elements")))          
##print(a)
##print(b)
##             
##for k in b:
##        if k not in a:
##            a.append(i)           
##print(a)






##a={'s1':45,'s2':98,"s3":69}
##for i in a:
##    print(i)
##    
##for i in a.keys():
##    print(i,a[i])
##    
##for i in a.values():
##    print(i)    
##
##for i,j in a.items():
##    print(i,j)







##a={'a':45,'b':87,'c':98}
##c=0
##for i in a.keys():
##    c+=1
##print(c)    




##a={}
##for i in range(2):
##    key=input("enter the keys")
##    val=[]
##    for j in range(3):
##        b=int(input("enter a values"))
##        val.append(b)
##    a[key]=val
##print(a)    


###-------------------------------------------> Functions <----------------------------------------------------------
##
##def add():      #function definition
##    a=10
##    b=20
##    print(a+b)
##
##
##add()           #function call
##
##add()
##
##add()
##




##
##def add():                                  #function definition
##    a=int(input("enter the number"))
##    b=int(input("enter the number"))
##    print(a+b)
##    
##add()                                       #function call



##def add():
##    a=int(input("enter the number"))
##    b=int(input("enter the number"))
##    return(a+b)
##    
##print(add())




##a=int(input("enter the number"))
##b=int(input("enter the number"))
##
##
##def add(a,b):            #formal parameters
##    return(a+b)
##
##print(add(a,b))           #actual parameters
##
##
##
##
##
##a=int(input("enter the number"))
##b=int(input("enter the number"))
##c=int(input("enter the number"))
##
##def add(a,b,c):
##    return(a+b+c)
##
##print(add(a,b,c))
##
##
##
##a=int(input("enter the number"))
##b=int(input("enter the number"))
##
##
##def add(n,m):
##    return(a+b)
##
##print(add(a,b))




##a=int(input("enter the number"))
##b=int(input("enter the number"))
##
##def add(a,b):
##    c=a+b
##    return(c)
##
##
##def sub(a,b):
##    c=a-b
##    return c
##
##print(add(a,b))
##print(sub(a,b))



###Q)prime number in function
##a=int(input("enter a number"))
##def prime(a):
##    c=0
##    for i in range(1,a+1):
##      if a%i==0:
##        c+=1
##    if c==2:
##        print("prime")
##    else:
##        print("not prime")
##
##prime(a)
##
##    
##
##
##a=int(input("enter a number"))
##def prime(a):
##    c=0
##    for i in range(1,a+1):
##      if a%i==0:
##        c+=1
##    if c==2:
##        return("prime")
##    else:
##        return("not prime")
##
##print(prime(a))





##print("1 for addition , 2 for subtraction , 3 for multiplication , 4 for division")
##a=int(input("enter a number for calculation\t"))
##
##n=int(input("enter a number\t"))
##m=int(input("enter a number\t"))
##
##def add(n,m):
##    return(n+m)
##def sub(n,m):
##    return(n-m)
##def mul(n,m):
##    return(n*m)
##def div(n,m):
##    return(n%m)
##
##if a==1:
##    print(add(n,m))
##elif a==2:
##    print(sub(n,m))
##elif a==3:
##    print(mul(n,m))
##elif a==4:
##    print(div(n,m))
##else:
##    print("enter valid input operation")





##print("1 for addition , 2 for subtraction , 3 for multiplication , 4 for division")
##a=int(input("enter a number for calculation\t"))
##
##n=int(input("enter a number\t"))
##m=int(input("enter a number\t"))
##
##
##def calculator(n,m):
##    if a==1:
##        return(n+m)
##    elif a==2:
##        return(n-m)
##    elif a==3:
##        return(n*m)
##    elif a==4:
##        return(n%m)
##    else:
##        print("enter a valid input")
##
##print(calculator(n,m))




##a=10             #global variable
##
##def sample():
##    a=11         #local variable
##    print(a)
##
##sample()
##print(a)    
##
##
##
##
##a=10              #global variable
##
##def sample():
##   print(a)
##
##sample()
##print(a)    
##
##
##
##a=10                 #global variable
##
##def sample():
##    a=11             #local variable
##    print("1st",a)
##
##sample()
##print('2nd',a)  





##a=10                 #global variable
##
##def sample():
##    b=22             #local variable
##    print("1st",b)
##
##sample()
##print('2nd',b)  




##a=10                 #global variable
##
##def sample():
##    b=22             #local variable
##    print("inside",a,b)
##
##sample()
##
##print('outside',a,b)  
##
##
##
##a=10                 #global variable
##
##def sample():
##    global b
##    b=22             #local variable
##    print("inside",b)
##
##sample()
##
##print('outside',b)  





##a=11
##print(a)
##def sample():
##    a=12
##    a+=1
##    print(a)
##
##sample()
##
##print(a)
##
##
##
##
##a=11
##print(a)
##def sample():
##    global a
##    a=12
##    a+=1
##    print(a)
##
##sample()
##
##print(a)




###Q)finding the before and after prime
##n=int(input("enter a number\t"))
##m=n+1
##lp=[]
##c=0
##for i in range(1,n+1):                #finding given number is prime are not
##    if n%i==0:
##        c+=1
##if c==2:
##    print(n,"is prime")
##else:
##    for i in range(n-1,1,-1):         #finding below prime 
##        cb=0
##        for j in range(1,i+1):
##            if i%j==0:
##                cb+=1
##        if cb==2:
##            lp.append(i)
##            break    
##    print("lower prime",lp[0])
##    
##    while m>1:                         #finding above prime
##            cu=0
##            for l in range(1,m+1):
##                if m%l==0:
##                    cu+=1
##            if cu==2:
##                lp.append(m)
##                break
##            m+=1        
##    print("upper prime",lp[1])
##            
##    if abs(n-lp[0])>abs(n-lp[1]):           #below prime and after prime
##                print("nearest prime is",lp[1])
##    elif abs(n-lp[0])<abs(n-lp[1]):
##                print("nearre prime is",lp[0])
##    else:
##          print("both are equal in distance",lp[0],lp[1])



###modules(mod.py)
##
##def add(a,b):
##    return (a+b)
##
##
##def sub(a,b):
##    return(a-b)




###----------------------------------------------> File handlings <-------------------------------------------------------------
##
##file=open("sample.txt","x")
##file.close()
##
##
##file=open(r"c:\users\N. R. Sirikonda\desktop\sample.txt","x")
##file.close()


###create the file after
##file=open(r"c:\users\N. R. Sirikonda\desktop\sample.txt","w")
##file.write("hi,good morning")
##file.close()


###create the file before
##file=open(r"c:\users\N. R. Sirikonda\desktop\sample.txt","w")
##file.write("hi,gopal")
##file.close()




##file=open(r"c:\users\N. R. Sirikonda\desktop\sample.txt","w")
##file.write("hi,gopal\t")
##file.write("good morning")
##file.close()



##file=open(r"c:\users\N. R. Sirikonda\desktop\sample.txt","r")
##a=file.read()
##print(a)



##file=open(r"c:\users\N. R. Sirikonda\desktop\sample.txt","a")
##file.write("this is file handling topic")
##file.close()



##file=open(r"c:\users\N. R. Sirikonda\desktop\sample.txt","r")
##a=file.read()
##print(a)



##file=open(r"c:\users\N. R. Sirikonda\desktop\sample.txt","r")
##a=file.readlines()
##c=0
##for i in a:
##    c+=1
##    print(c,i)



##file=open(r"c:\users\N. R. Sirikonda\desktop\sample.txt","r")
##a=file.readlines()
##for i in a:
##    print(i)




##file=open(r"c:\users\N. R. Sirikonda\desktop\example.py","w")
##file.write("hi,gopal")
##file.close()



###Q)factorial of a number
##
##def factorial(n):#5
##    fact=1
##    for i in range (1,n+1):  #(1,6) 
##        fact=fact*i #1=1*1 , 1=1*2 , 2=2*3 , 6=6*4 , 24=24*5
##    return(fact) # 120
##
##n=int(input("enter the number\t"))
##print(factorial(n))
##            
##
##
##def factorial(n):
##    fact=1
##    for i in range (n,0,-1):   
##        fact=fact*i
##    return(fact)
##
##n=int(input("enter the number\t"))
##print(factorial(n))





##def factorial(n): # 5
##    if n==1: #5!=1 , 4!=1 , 3!=1 , 2!=1 , 1==1
##        return 1
##    else:
##        return(n*factorial(n-1)) #5*(5-1)=5*4=20 , 20*3=60 , 60*2=120 , 120*1=120
##
##n=int(input("enter the number\t"))    
##print(factorial(n))




      
###Q)simple monthly calendar
##import calendar
##yy=int(input("enter the year\t"))
##mm=int(input("enter the month\t"))
##
##print(calendar.month(yy,mm))



#Q)print the stars
##n=int(input("enter the number\t"))
##for i in range(1,n+1):
##    print('*'*i)
##
##
##
##n= int(input("enter the number\t"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print('*',end=" ")
##    print()   
##
##
##n=int(input("enter the number"))
##c=0
##while n:
##    n-=1
##    c+=1
##    print(''*n,'*'*c)
##
##
##
##
##
##n=int(input("enter the number\t"))  # 3
##k=2*n-2  # 4  2
##for i in range(0,n):  # (0,3)
##    for j in range(0,k):  # (0,4)
##        print(end=" ")
##    k-=2
##    for j in range(0,i+1):  # (0,1)
##        print("*",end=" ")  #  *
##    print()    
##
##
##
##
##n=int(input("enter the number\t"))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==int((n+1)//2):
##            print('*',end="")
##        elif i!=int((n+1)//2) and j==int((n+1)//2):
##            for k in range(1,n+1):
##                if k==int((n+1)//2):
##                    print('*',end="")
##                else:
##                    print(' ',end="")
##
##    print()                    
##
##
##
##
##
##n=int(input("enter a number\t"))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or i==n:
##            print('*',end="")
##        else:
##            if j==1 or j==n:
##                print('*',end="")
##            else:
##                print(' ',end='')
##    print()           
##
##n=int(input("enter the number\t"))
##for i in range(1, n+1):
##    for j in range(1, n+1):
##        if(i == 1 or i == n or j == 1 or j == n):
##            print('*',end= "")
##        else:
##            print(" ",end= "")
##    print()        
##
##
##
##n=int(input('enter the number\t'))
##for i in range(1, n + 1):               #no of rows
##    for j in range(1, n - i + 1):       #print empty spaces
##        print(end=" ")                  #print empty spaces
##    if i == 1 or i == n:                #print the stars in first and last row
##        for j in range(1, n + 1):       #print the stars in first and last row
##            print("*",end="")           #print the stars in first and last row   
##    else:
##        for j in range(1,n+1):
##            if(j == 1 or j == n):
##                print("*",end="")
##            else:
##                print(end=" ")
##    print()        





###------------------------------------------> Error / Exception handling <-------------------------------------------------------
##a=10
##print(a+10)


##a=10
##print(a/0)




##a=10
##try:
##    print(a+b)
##except:
##    print("some un excepted error")





##a=10
##try:
##    print(a/0)
##except:
##    print("some un excepted error")




##a=10
##try:
##    print(a/0)
##except NameError :
##    print("some un excepted error")
##except ZeroDivisionError:
##    print("forget about this error")





##try:
##    f=open("file.csv","r")
##    a=f.read()
##    print(a)
##except:
##    print("no file")






##try:
##    f=open(r'c:\users\N. R. Sirikonda\Desktop\sample.txt','r')
##    a=f.read()
##    print(a)
##except:
##    print('no file')
##else:
##    print("no error in try block")
##finally:
##    print("excute it any way")















 
















