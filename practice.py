
##a=int(input("enter a number"))
##b=float(input("enter a float"))
##c=input("enter a string")
##print(a,type(a))
##print(b,type(b))
##print(c,type(c))
##
##
##
##
##imid="gopal@cricket.com"
##ipwd="2020"
##
##mid=input("enter a mail id")
##pwd=input("enter a password")
##if imid==mid and ipwd==pwd:
##    print("login successful")
##else:
##    print("wrong mail id or password")



##option=[]
##for i in range(5):
##    opt=int(input("enter the option"))
##    option.append(opt)
##print(option)
##cnt=0
##con=0
##answer=[]
##for j in range(5):
##  ans=input("enter your option")
##  answer.append(ans)
##  print(answer)  
##  if option==ans:
##    cnt=cnt+1
##    print(cnt,"yes")
##  elif option!=ans:
##    con=con+1
##    print(con,"no")



##a=[]
##for i in range (5):
##    b=int(input("enter the options"))
##    a.append(b)
##print(a)
##cnt=0
##con=0
##c=[]
##for j in range(5):
##    d=int(input("enter the your option"))
##    c.append(d)
##    print(c)
##    for k in a:
##     if c==a:
##        cnt+=1
##        print(cnt,"yes")
##     if c!=a:
##        con+=1
##        print(con,"no")
    
##for k in a:
##       if c[j]==a[i]:
##        cnt=cnt+1
##        print(cnt,"yes")
##       elif c[j]!=a[i]:
##        con=con+1
##        print(con,"no")



##cnt=0
##con=0
##for a in range(0,5):
##  ans=input("enter your option")
##  if ans==a:
##    cnt=cnt+1
##    print(cnt,"yes")
##  if ans!=a:
##    con=con+1
##    print(con,"no")






##iacc='12345' 
##ipin='112233'
####nacc='678910'
####npin='445566'
##
##acc=input("enter the your account number\t")
##pin=input("enter the your pin\t")
##if iacc==acc and ipin==pin :#or nacc==acc and npin==pin:
##    print("login success")
##elif iacc!=acc and ipin!=pin :#or  nacc!=acc and npin!=pin:
##    print("wrong account number and pin ")
##    print("please check")    
##elif iacc!=acc :#or nacc!=acc:
##    print("wrong account number")
##    print("please check")
##elif ipin!=pin :#or npin!=pin:
##    print("wrong pin")
##    print("please check")


##a=int(input("enter a number\t"))
##b=float(input("enter a float\t"))



##imid="gopal@cricket.com"
##ipwd="2020"
##
##mid=input("enter a mail id\t")
##pwd=input("enter a password\t")
##if imid==mid and ipwd==pwd:
##    print("login successful")
##else:
##    print("wrong mail id or password")
##
##
##
##
##
##import calendar
##yy=int(input("enter a year\t"))
##mm=int(input("enter a month\t"))
##print(calendar.month(yy,mm))    



##a=int(input("enter a"))
##b=int(input("enter b"))
##c=a+b
##print(c)




##for i in range(2,5,1):
##    print(i)

    


##for i in range(0,5):
##    print(i)
##






##n=int(input("enter the number "))
##c=0
##for i in range(1,n+1):
##    if n%i==0:
##        c+=1        
##if c==2:
##    print("prime")
##else:
##    print("not prime")

##n=(int(input("enter a number \t"))
##   for i in range(0,5)
##   while n%2!=0:
##    print("number is odd")
##    break
##
##print("number is even")
##


##n=int(input("enter the range"))
##for i in range(2,n+1):
##    if n%i==0:
##        print("even")
##else:
##    print("odd")



##
##n=int(input())  # 3
##for i in range(n):  # 3
##    for j in range(i+1):   # 0+1=1    1+1=2   2+1=3
##        print('*',end=' ')  #  *        **      ***
##    print()  #nl  nl
##    
##n=int(input())
##for i in range(n):
##    for j in range(n):
##        print('#',end=' ')
##    print()
##
##n=int(input())  # 3
##for i in range(n):  # 3
##    for j in range(n-i):   #  3-0=3   3-1=2   3-2=1
##        print('*',end=' ')  #   ***     **      *
##    print()  #nl   nl
##
##n=int(input())
##k=2*n-2
##for i in range(0,n):
##    for j in range(0,k):
##        print(end=' ')
##    k-=2
##    for j in range(i+1):
##        print("*",end=' ')
##    print()    




##a=[]
##n=int(input())
##
##for i in range(n):
##    b=int(input())
##    a.append(b)
##print(a)



##
##n=10
##seive=[i for i in range (n+1)]
##seive[0]=0
##seive[1]=0
##for i in range(2,n+1):
##    if seive[i]==i:
##        if (seive[i]%2)==0:
##            seive[i]=0
##            print(i,"even")
##print(seive)




    
##n=int(input())
##seive=[i for i in range(n+1)]
##seive[0]=0
##seive[1]=0
##for i in range(2,n+1):
##    if (seive[i]%2)!=0:
##        seive[i]=i
##        print(i,"prime")
##    else:
##        print(i,"not prime")
##        
##print(seive)





##n=int(input())
##seive=[i for i in range(n+1)]
##seive[0]=0
##seive[1]=0
##c=0
##for i in range(2,n+1):
##       if seive[i]==i:
##            for j in range(2,10):
##                if (seive[i]%j)==0:
##                    c+=1        
##            if c==2:
##                 seive[i]=seive[i]
##                 print(i,"prime")
##         
##print(seive)        




##def seive(n):
##    seive=[i for i in range(0,n+1)]
##    seive[0]=0
##    seive[1]=0
##    i=2
##    c=0
##    for i in range(2,n+1):
##        if seive[i]==i:
##            if (seive[i]%2)==0:
##                print(i,end=' ')
##                seive[i]=1
##            else:
##                seive[i]=0
##        if seive[i]==1:
##            c+=1        
##    print('\n',c)       
##    print(seive)
##n=int(input())
##print("Even=1","odd=0")
##seive(n)
     

###-------------------> prime or not AND even or odd with functions <-------------------------
                
##def evod(n):
##    if n%2==0:
##        return 1
##    else:
##        return 0
##
##n=int(input())
##print(evod(n))
##
##
##
##def prinot(x):
##    c=0
##    for i in range(1,x+1):
##        if x%i==0:
##            c+=1
##    if c==2:
##        return 1
##    else:
##        return 0
##
##x=int(input())
##print(prinot(x))
##
##
##
##
##def evod(x):
##    if x%2==0:
##        print("Even")
##    else:
##        print("Odd")
##    print("AND")    
##def prinot(x):
##    c=0
##    for i in range(1,x+1):
##        if x%i==0:
##            c+=1
##    if c==2:
##        print("prime")
##    else:
##        print("not prime")
##
##x=int(input())
####x=int(input())
##evod(x)
##prinot(x)



##n=int(input())
##arr1=[]
##arr2=[]
##for i in range(0,n):
##    z=int(input())
##    arr1.append(z)
##for j in range(0,n):
##    x=int(input())
##    arr2.append(x)
##print(arr1)
##print(arr2)    









##class phone:
##    def __init__(self):
##        pass
##s1=phone()
##
##
##
##class servey:
##    def __init__(self,name,phno,num,address):
##        self.name=name
##        self.phno=phno
##        self.num=num
##        self.address=address
##        print(self.name,self.phno,self.num,self.address)
##
##p1=servey('gopal',12345678910,5,'santhi nagar')
##
##
##class phone:
##    made='India'
##    def __init__(self,company,model,storage):
##        self.company=company
##        self.model=model
##        self.storage=storage
####        self.made="KKD"
##    def display(self):
####        self.made="KKD"
##        print(self.company,self.model,self.storage,self.made)
##
##
##ph1=phone('oppo','A5','128gb')
##ph1.display()        

        
        

##class phone:
##    made='India'
##    def __init__(self,company,model,storage):
##        self.company=company
##        self.model=model
##        self.storage=storage
##    def display(self):
##        print(self.company,self.model,self.storage,self.made)
##
##a=input("Enter the phone company you want\t")
##b=input("Enter the phone model you want\t")
##c=input("Enter the phone storage you want\t")
##ph1=phone(a,b,c)
##ph1.display()        



##class phone:
##    made='India'
##    def __init__(self,company,model,storage):
##        self.company=company
##        self.model=model
##        self.storage=storage
##    def display(self):
##         print(self.company,self.model,self.storage,self.made)
##    @classmethod
##    def classmethod(cls):
##        print('hai')
##    
##
##ph1=phone('oppo','A5','128gb')
##ph1.display()        
##ph1.classmethod()




##class phone:
##    made='India'
##    def __init__(self,company,model,storage):
##        self.company=company
##        self.model=model
##        self.storage=storage
##    def display(self):
##         print(self.company,self.model,self.storage)
##    @classmethod
##    def classmethod(cls):
##        print("class method")
##    @classmethod
##    def classmethod(cls):
##        print(cls.made)
##        cls.classmethod()
##        
##    
##
##ph1=phone('oppo','A5','128gb')
##ph1.display()        
##ph1.classmethod()
##
##




##a=[47,58,61,448,325,1,24,69,1158,47,635,6]
##for i in range(0,12):
##    a.sort()
##    print('Index:',i,'Values:',a[i])
##print(a)
##a.reverse()
##print(a)
##
##
##n=int(input("Enter how many elements you want"))
##a=[]
##for i in range (n):
##    b=int(input("Enter the elements"))
##    a.append(b)
##    a.sort()
##    print("Index:",i,'Value:',a[i])
##print('Total Indexs:',i,"Total Values:",n,a)



##n=int(input("Enter how many elements you want"))
##a=[]
##for i in range (n):
##    b=int(input("Enter the elements"))
##    a.append(b)
##    print("Index:",i,'Value:',a[i])
##print("Before sorting",a)
##a.sort()
##a.reverse()
##print(a)
##print("After sorting",a)
##print('Total Indexs:',i,"Total Values:",n)



##a=[1,2,3,4,6,7,8,9]
##print('"Original:"',a)
##print()
##a.reverse()
##print('Reverse:',a)
##print()
##a.sort()
##print('Sort:',a)
##print()
##a.append(10)
##print('Append:',a)
##print()
##a.insert(4,5)
##print('Insert Index 4,Value 5 is:',a)
##print()
##a.pop()
##print('Pop:',a)
##print()
##a.remove(9)
##print('Remove value 9 is:',a)
##print()
##a.clear()
##print('Clear:',a,)
##print()
##
##
##a=[1,2,3,4,5,6,7,8,9,10]
##print('"Original:"',a)
##print()
##print('Len:',len(a))
##print()
##print('Max:',max(a))
##print()
##print("Min:",min(a))
##print()
##print("Count of 3 is:",a.count(3),'time')
##print()
##print("Index of 3 is:",a.index(3),"Position")
##print()
##del a[1]
##print("Del of Index of 1 is:",a)
##print()
##
##a=[1,2,3,4,5,6,7,8,9,10]
##print('"Original values of a:"',a)
##print()
##b=[11,12,13,14,15]
##print('"Original values of b:"',b)
##print()
##a.extend(b)
##print("Extend:",a)





##a=[1,2,3,4,5]
##print("The original list is: "+ str(a))
##a.insert(0,a.pop())
##print("The list after shift is: " + str(a))
##
##
##a=[1,2,3,4,5]
##print("The original list is: "+ str(a))
##a=a[-1:] + a[:-1]
##print("The list after shift is: " + str(a))





##a=[1,2,3,4,5]
##b=a[-1:]+a[:-1]
##a.insert(0,a.pop())
##print(a)
##print(b)



### ------------------------------------> Create a matrix <-----------------------------------
##r=int(input())
##c=int(input())
##matrix=[]
##print("Enter the entries rowwise:")
##for i in range(r):
##    a=[]
##    for j in range(c):
##        a.append(int(input()))
##    matrix.append(a)
##for i in range(r):
##        for j in range(c):
##                 print(matrix[i][j],end=' ')
##        print()         
##                 
##
##import numpy as np
##r=int(input())
##c=int(input())
##print("Enter the entries in a single line (separated by space):")
##entries=list(map(int,input().split()))
##matrix=np.array(entries).reshape(r,c)
##print(matrix)
##
##
##mat=[[int(input()) for x in range(c)] for y in range(r)]
##matrix=[]
##print("Enter the entries rowwise:")
##a=[]
##for j in range(c):
##    a.append(int(input()))
##    matrix.append(a)
##for j in range(c):
##                 print(matrix[i][j],end=' ')
##print()         







"""
OOPS
class , object, @classmethod , @instancemethod
"""

##class Employee:
##    company="India pvt.ltd"
##    def __init__(self,idno,name,phno,company):
##        self.idno=idno
##        self.name=name
##        self.phno=phno
##        self.company="BPRGA pvt.ltd"
##    def display(self):
##        print(self.idno,self.name,self.phno,self.company)
##    @classmethod
##    def classmethod(self):
##        print(self.company)
##    @staticmethod
##    def static():
##        print("HELLO")
##        
##
##    
##emp1=Employee(1,"kishore",12345678910,"Gopal pvt.ltd")
##emp1.display()
##emp1.classmethod()
##emp1.static()



"""
SINGLE INHERITANCE:-------------------->

             parent class
                   |
             child class      
"""
##class Employee:
##    def __init__(self,idno,name,phno,company):
##        self.idno=idno
##        self.name=name
##        self.phno=phno
##        self.company=company
##    def display_1(self):
##        print(self.idno,self.name,self.phno,self.company)
##
##class Person(Employee):
##    def __init__(self,idno,name,phno,company,dept):
##        super().__init__(idno,name,phno,company)
##        self.dept="MACHINE WORKER"
##    def display_2(self):
##        print(self.idno,self.name,self.phno,self.company,self.dept)
##
####emp1=Employee(1,"RAJU","1112131415","Chinnu PVT.LTD")
####emp1.display_1()
##emp1=person(1,"RAJU","1112131415","Chinnu PVT.LTD","Worker")
##emp1.display_2()



"""
HIRERICAL INHERITANCE:------------------->

              parent class
                   |
        ------------------------
        |                      |
     child_1 class         child_2 class
"""

##class Employee:
##    def __init__(self,idno,name,phno,company):
##        self.idno=idno
##        self.name=name
##        self.phno=phno
##        self.company="GOPAL PVT.LTD"
##    def display_1(self):
##        print(self.idno,self.name,self.phno,self.company)
##class Person(Employee):
##    def __init__(self,idno,name,phno,company,dept):
##        super().__init__(idno,name,phno,company)
##        self.dept="MACHINE WORKER"
##    def display_2(self):
##        print(self.idno,self.name,self.phno,self.company,self.dept)
##class Salary(Employee):
##    def __init__(self,idno,name,phno,company,sal):
##        super().__init__(idno,name,phno,company)
##        self.sal=150000
##    def display_3(self):
##        print(self.idno,self.name,self.phno,self.company,
##              self.sal)
##
##emp1=Employee(1,"RAJU","1112131415","CHINNU PVT.LTD")
##emp1.display_1()
##print("Parent class")
##emp2=Person(2,"RAMESH","12345678910","CHINNU PVT.LTD","MAKER")
##emp2.display_2()
##emp2.display_1()
##emp1.display_1()
##print("child_1 class")
##emp3=Salary(3,"JAGADESH","12345678910","CHINNU PVT.LTD",100000)
##emp3.display_3()
##emp1.display_1()
##emp3.display_1()
##print("child_2 class")



"""
MULTI-LEVEL INHERITANCE:------------------->

              grand parent class              
                     |                            
               parent class
                     |
              child_1 class    
"""
##class Employee:
##    def __init__(self,idno,name,phno,company):
##        self.idno=idno
##        self.name=name
##        self.phno=phno
##        self.company=company
##    def display_1(self):
##        print(self.idno,self.name,self.phno,self.company)
##class Person(Employee):
##    def __init__(self,idno,name,phno,company,dept):
##        super().__init__(idno,name,phno,company)
##        self.dept="MACHINE WORKER"
##    def display_2(self):
##        print(self.idno,self.name,self.phno,self.company,self.dept)
##class Salary(Person):
##    def __init__(self,idno,name,phno,company,dept,sal):
##        super().__init__(idno,name,phno,company,dept)
##        self.sal=sal
##    def display_3(self):
##        print(self.idno,self.name,self.phno,self.company,self.dept,self.sal)
##emp=Salary(4,"BABJI","10987654321","GOPAL PVT.LTD","CLERK",150000)
##emp.display_3()
##emp.display_2()
##emp.display_1()
                

"""
MULTIPLE INHERITANCE:----------------------->

parent class                parent class
    |                            |
    -----------------------------
                 |
              child class
                 
"""
##class Employee:
##    def __init__(self,idno,name,phno,company):
##        self.idno=idno
##        self.name=name
##        self.phno=phno
##        self.company=company
##    def display_1(self):
##       print(self.idno,self.name,self.phno,self.company)
##class Person(Employee):
##    def __init__(self,dept):
##        self.dept=dept
##    def display_2(self):
##        print(self.dept)
##class Family(Employee,Person):
##   pass
##emp=Family(5,"PRASAD","12365478910","GOPAL PVT.LTD","MACHINE WORKER")
##print(emp.name)
##emp=display_1()


"""
------------------------------------------------------------------------> YOUTUBE <------------------------------------------------------------------------------
***************************************************************************************************************************************************************
#############################################################################################################################################################
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
###------------------------------------------------> Number Systems <--------------------------------------------------------------

#####  Decimal To Binary (0b)
##a=bin(25)
##print(a)
##
#####  Binary To Decimal
##w=0b0101
##print(w)
##
#####  Decimal To Octal (0o)
##z=oct(25)
##print(z)
##
##
#####  Decimal To Hexadecimal(0X)
##q=hex(25)
##print(q)
##
##
#####  Hexadecimal To Decimal
##s=0xf
##print(s)





### Swap Two Numbers
##a=5
##b=6
##temp=a
##a=b
##b=temp
##print(a,b)
##
##
##
##a=5
##b=6
##a=a+b
##b=a-b
##a=a-b
##print(a)
##print(b)
##
##
##a=5
##b=6
##a=a^b
##b=a^b
##a=a^b
##print(a)
##print(b)
##
##
##a=5
##b=6
##a,b=b,a
##print(a)
##print(b)




###-----------------------------------------------------> OPERATORS <--------------------------------------------------------
###complement Operator
##a=~12
##print(a)
##
##a=~12
##print(abs(a))


### Bitwise AND
##b= 12&13
##print(b)
### Bitwise OR
##c= 12|13
##print(c)
### Bitwise XOR
##s=12^13
##print(s)




### Left Shift
##e=10<<2
##print(e)
### Right Shift
##w=10>>2
##print(w)



### Importing Functions
##import math
##x=math.sqrt(29)
##print(x)
##print(math.floor(x))
##print(math.ceil(x))




##import math as m
##q=m.sqrt(25)
##print(q)


##from math import sqrt
##w=sqrt(25)
##print(w)





##ch=input("enter the character")
##print(ch)
##
##
##ch=input("enter the character")
##print(ch[0])
##
##
##ch=input("enter the character")[0]
##print(ch)



##result=eval(input('enter an expression'))
##print(result)



##from array import *
##
##vals=array('i',[5,9,8,4,2])
##print(vals)


##from array import *
##
##arr=array('i',[])
##n=int(input("enter the length of the array"))
##for i in range(n):
##    x=int(input("enter the next value"))
##    arr.append(x)
##print(arr)
##val=int(input("enter the value for search"))
##k=0
##for e in arr:
##    if e==val:
##        print(k)
##        break
##    k+=1


###-----------------------------------------------------> MATRIX <-------------------------------------------------------
##from numpy import *
##arr=array([1,2,3,2,5,4])
####print(arr)
##
##
##
##
##from numpy import *
##arr=array([1,2,3,4,5.0])
##print(arr.dtype)
##
##
##
##
##from numpy import *
##arr1=array([1,2,3,4,5])
##arr2=array([6,7,8,9,10])
##arr3=arr1+arr2
##print(arr3)
##
##
##
##from numpy import *
##arr1=array([1,2,3,4,5])
##arr2=array([6,7,8,9,10])
##print(concatenate([arr1,arr2]))
##
##
##
##from numpy import *
##arr1=array([1,2,3,4,5])
##arr2=arr1
##print(arr1,arr2)




##
##from numpy import *
##arr1=array([[1,2,3],[4,5,6]])
##print(arr1)
##print(arr1.dtype)
##print(arr1.ndim)  # dimensation
##print(arr1.shape)
##print(arr1.size)
##
##
##
##
##
##
##from numpy import *
##arr1=array([[1,2,3],[4,5,6]])
##arr2=arr1.flatten()
##print(arr2)
##
##
##
##
##
##from numpy import *
##arr1=array([[1,2,3,6,2,9],[4,5,6,7,5,3]])
##arr2=arr1.flatten()
##arr3=arr2.reshape(3,4)
##print(arr3)
##print(arr2)
##
##
##from numpy import *
##arr1=array([[1,2,3,6,2,9],[4,5,6,7,5,3]])
##arr2=arr1.flatten()
##arr3=arr2.reshape(2,2,3)
##print(arr3)
##
##
##
##
##from numpy import *
##arr1=array([ [1,2,3,6],[4,5,6,7]])
##m=matrix(arr1)
##print(m)





##from numpy import *
##m=matrix('1 2 3 6 ; 4 5 6 7')
##print(m)
##
##from numpy import *
##m=matrix('1 2 ; 3 6 ; 4 5 ; 6 7')
##print(m)
##
##
##from numpy import *
##m=matrix('1 2  3  ;6  4 5 ;1 6 7')
##print(m)
##
##
##
##from numpy import *
##m=matrix('1 2  3  ;6  4 5 ;1 6 7')
##print(diagonal(m))
##print(m.max())
##print(m.min())



##from numpy import *
##m1=matrix('1 2 3 ; 6 4 5 ; 1 6 7')
##m2=matrix('1 2 3 ; 6 8 5; 2 6 7')
##m3=m1*m2
##print(m3)

###------------------------------------------------------> FUNCTIONS <-------------------------------------------------------------


##def greet():
##    print("Hello")
##    print("Good Morning")
##
##greet()
##
##
##def add(x,y):  # x,y are ARGUMENTS
##    c=x+y
##    print(c)
##
##add(1,2)
##
##
##def add(x,y): 
##    c=x+y
##    return c
##result=add(5,4)
##print(result)




##def add_sub(x,y):
##    c=x+y
##    d=x-y
##    return c,d
##result1,result2=add_sub(5,4)
##print(result1,result2)



###FUNCTION ARGUMENTS ------------------>

##def update(x):
##    x=8
##    print("x",x)
##
##    
##a=10
##update(a)
##print("a",a)



##def update(x):
##    print(id(x))
##    x=8
##    print(id(x))
##    print("x",x)
##
##    
##a=10
##print(id(a))
##update(a)
##print("a",a)



##def person(name,age): # a,b are formal arguments
##    print(name)
##    print(age)
##
##person('navin',28) #actual arguments
##
##
##### types of actual arguments
##def person(name,age):
##    print(name)
##    print(age)
##
##person('navin',28) # positional arguments
##person(age=28,name='navin')  # keyword arguments
##
##
##
##def person(name,age=18):
##    print(name)
##    print(age)
##
##
##person('navin') # default arguments
##
##
###variable length argument
##def sum(a,*b):
##    c=a
##    for i in b:
##        c=c+i
##    print(c)
##    
##sum(5,6,34,78)


##
###keyworded variable length arguments
##def person(name,**data):
##    print(name)
##    print(data)
##    
####    for i,j in data.items():
####        print(i,j)
##
##
##
##person('navin',age=28,city='mumbai',mobile=9865432)





##a=10 # global variable
##def something():
##    a=20          # local variable
##    print(a)
##something()    
##print(a)
##
##
##
##a=10 # global variable
##def something():
##    global a
##    a=20          # local variable
##    print(a)
##something()    
##print(a)
##
##
##
##
##a=10 
##def something():
##    a=20
##    x=globals()['a']
##    print(a)
##something()    
##print(a)
##
##
##
##a=10 
##def something():
##    a=20
##    x=globals()['a']
##    print(a)
##    globals()['a']=15
##something()    
##print(a)

















##def count(lst):
##    even=0
##    odd=0
##    for i in lst:
##        if i%2==0:
##            even+=1
##        else:
##            odd+=1
##    return even,odd         
##
##
##lst=[20,25,14,19,16,24,28,47,26]
##even,odd=count(lst)
##print(even)
##print(odd)
##print("Even :{} and odd: {}".format(even,odd))





###-------------> Fibonacci Sequence
##
##
##def fib(n):
##    a=0
##    b=1
##
##    if n==1:
##        print(a)
##    elif n<=0:
##        print("Invalid")
##    else:    
##        print(a)
##        print(b)
##
##        for i in range(2,n):
##            c=a+b
##            a=b
##            b=c
##            print(c)
##            
##fib()




###-------------> Factorial of a number
##
##
##def fact(n):
##    f=1
##    for i in range(1,n+1):
##        f=f*i
##    return f
##x=10
##result=fact(x)
##print(result)
        
    




###--------------------> Recursion
##
##
##import sys
##print(sys.getrecursionlimit())
##
##i=0
##def greet():
##    global i
##    i+=1
##    print("Hello",i)
##    greet()
##    
##
##greet()    



###---------------------->Factorial Using Recursion
##
##
##def fact(n):
##    if (n==0):
##        return 1
##    return n* fact(n-1)
##n=int(input())
##result=fact(n)
##print(result)



###functions without name (or) anonymous function--------------->
##
##f=lambda a: a*a
##result=f(5)
##print(result)
##
##
##f=lambda a,b: a+b
##result=f(5,6)
##print(result)


###filter function:--------------->
##def is_even(n):
##    return n%2==0
##nums=[3,2,5,7,9,6,4,8]
##evens=list(filter(is_even,nums))
##print(evens)

##nums=[6,5,8,9,4,2]
##evens=list(filter(lambda n: n%2==0,nums))
##print(evens)


###map function:----------------------->
##def update(n):
##    return n*2
##nums=[6,5,8,9,4,2]
##evens=list(filter(lambda n: n%2==0,nums))
##doubles=list(map(update,evens))
##print(evens)
##print(doubles)
##
##
##
##nums=[6,5,8,9,4,2]
##evens=list(filter(lambda n: n%2==0,nums))
##doubles=list(map(lambda n: n*2,evens))
##print(evens)
##print(doubles)





###reduce function:------------->
##
##from functools import reduce
##def add_all(a,b):
##    return a+b
##
##nums=[6,5,8,9,4,2]
##evens=list(filter(lambda n: n%2==0,nums))
##doubles=list(map(lambda n: n*2,evens))
##sum=reduce(add_all,doubles)
##print(evens)
##print(doubles)
##
##
##
##
##from functools import reduce
##nums=[6,5,8,9,4,2]
##evens=list(filter(lambda n: n%2==0,nums))
##doubles=list(map(lambda n: n*2,evens))
##sum=reduce(lambda a,b:a+b,doubles)
##print(evens)
##print(doubles)





##def div(a,b):
##    print(a/b)
##
##div(4,2)
##div(2,4)
##
##
##
##
##def div(a,b):
##    if a<b:
##        a,b=b,a
##        
##    print(a/b)
##
##div(4,2)
##div(2,4)



###decorater------------------>
##def div(a,b):
##    print(a/b)
##
##
##def smart_div(func):
##    def inner(a,b):
##        if a<b:
##            a,b=b,a
##        return func(a,b)
##    return inner
##div=smart_div(div)
##div(2,4)




##from mod import *
##import mod
##a=9
##b=7
##c=add(a,b)
##print(c)




###-----------------------------> Object Oriented Program (OOPs) <---------------------------------------

##
##class computer:
##    def config(self):
##        print("i5,16gb,1tb")
##        
##a=5
##print(type(a))
##comp1=computer()
##print(type(comp1))


##
##class computer:
##    def config(self):
##        print("i5,16gb,1tb")
##
##
##comp1=computer()
##computer.config(comp1)
##
##comp2=computer()
##computer.config(comp2)
##
##comp1.config()
##comp2.config()



##class computer:
##    def __init__(self,cpu,ram):
##        self.cpu=cpu
##        self.ram=ram
##    def config(self):
##        print("config is", self.cpu,self.ram)
##
##comp1=computer("i5",16)
##comp2=computer('Ryram 3',8)
##comp1.config()
##comp2.config()


##
##class computer:
##    def __init__(self):
##        self.name='gopal'
##        self.age=20
##    def update(self):
##        self.age=25
##
##c1=computer()
##print(c1.name)
##c1.update()
##c1.name='chinnu'
##print(c1.name)



##
##class car:
##    wheels=4                     # class variable
##    def __init__(self):          # constructer (__init__)
##        self.mil=10              # instance variable
##        self.com='BMW'           # instance variable
##
##
##c3=car()
##c2=car()
####c3.mil=8
####car.wheels=5
##print(c3.com,c3.mil,c3.wheels)
##print(c2.com,c2.mil,c2.wheels)



##class student:
##    school="ABC"                               # Class Variable
##    def __init__(self,m1,m2,m3):               # Constructor
##        self.m1=m1                             # Insistance Variable
##        self.m2=m2                             # Insistance Variable
##        self.m3=m3                             # Insistance Variable
##    def avg(self):
##        return(self.m1+self.m2+self.m3)/3
##    def get_m1(self):                          # Getters (can't change value)
##        return self.m1
##    def set_m1(self,value):                    # Setters (can change value)
##        self.m1=value
##    @classmethod                               # Class Method (to call class variable)
##    def info(cls):
##        return cls.school
##    @staticmethod                              # Static Method (it is user control)
##    def info():
##        print("this is student class.. in abc modules")
##
##        
##a1=student(58,98,47)
##a2=student(78,98,88)
##print(a1.m1)
##print(a2.m1)
##print(a1.avg())
##print(a2.avg())
##student.info()




###----------------------------------> Inner class <-------------------------------------------


##class student:                            # outer class
##    def __init__(self,name,rollno):
##        self.name=name
##        self.rollno=rollno
##        self.lap=self.laptop()
##
##    def show(self):
##       print(self.name,self.rollno)
##       self.lap.show()
##
##    class laptop:                         # inner class
##       def __init__(self):
##           self.brand='hp'
##           self.cpu='i5'
##           self.ram=8
##       def show(self):
##           print(self.brand,self.cpu,self.ram)
##           
##
##
##s1=student('raju',2)
##s2=student('jenny',3)
##s1.show()


###----------------------------------------> Inheritance <---------------------------------------------
### Inheritance : using features of existing class.
### Sub class can access all the features of Super class.


###Single Level Inheritance--------------> class B  using features of existing class A
##
##class A:                                    # super class
##    def feature1(self):
##        print("Feature 1 working")
##    def feature2(self):
##        print("Feature 2 working")
##
##class B(A):                                 # sub class
##    def feature3(self):
##        print("Feature 3 working")
##    def feature4(self):
##        print("Feature 4 working")
##
##
##      
##        
##a1=A()
##a1.feature1()
##a1.feature2()
##b1=B() # B can access the class A
##b1.feature1()
##b1.feature2()
##b1.feature3()
##b1.feature4()


###Multi-Level Inheritance---------------------> class B  using features of existing class A & class C  using features of existing class B
##
##class A:                                    # super class
##    def feature1(self):
##        print("Feature 1 working")
##    def feature2(self):
##        print("Feature 2 working")
##
##class B(A):                                 # sub class
##    def feature3(self):
##        print("Feature 3 working")
##    def feature4(self):
##        print("Feature 4 working")
##      
##class C(B):                                 # sub class
##    def feature5(self):
##        print("Feature 5 working")        
##a1=A()
##a1.feature1()
##a1.feature2()
##b1=B()# B can access the class A
##b1.feature1()
##b1.feature2()
##b1.feature3()
##b1.feature4()
##c1=C() # c can access the class B (nothing but class B & A because class B access class A)
##c1.feature1()
##c1.feature2()
##c1.feature3()
##c1.feature4()
##c1.feature5()

###Multiple Inheritance------------------------------> class C  using features of existing class A & class B
##
##class A:                                    # super class
##    def feature1(self):
##        print("Feature 1 working")
##    def feature2(self):
##        print("Feature 2 working")
##
##class B:                                   
##    def feature3(self):
##        print("Feature 3 working")
##    def feature4(self):
##        print("Feature 4 working")
##      
##class C(A,B):                                 # sub class
##    def feature5(self):
##        print("Feature 5 working")        
##a1=A()
##a1.feature1()
##a1.feature2()
##b1=B()  # B cann't access class A
##b1.feature3()
##b1.feature4()
##c1=C()  # c can access both class A & B
##c1.feature1()
##c1.feature2()
##c1.feature3()
##c1.feature4()
##c1.feature5()


### Constructor in Inheritance----------------------->
### If you create object of Sub class it will first try find init of Sub class, If it is not found then it will call init of Super class.
### To represent Super class we use super().__init__()

##class A:                                    # super class
##    def __init__(self):
##        print("in A init")
##    def feature1(self):
##        print("Feature 1 working")
##    def feature2(self):
##        print("Feature 2 working")
##
##class B(A):                                 # sub class
##    def __init__(self):
####        super().__init__()
##        print("in B init")
##    def feature3(self):
##        print("Feature 3 working")
##    def feature4(self):
##        print("Feature 4 working")
##
##
##a1=B()



##class A:                                    # super class
##    def __init__(self):
##        print("in A init")
##    def feature1(self):
##        print("Feature 1-A working")
##    def feature2(self):
##        print("Feature 2 working")
##
##class B:                                 # sub class
##    def __init__(self):
##        print("in B init")
##    def feature3(self):
##        print("Feature 3 working")
##    def feature4(self):
##        print("Feature 4 working")
##
##class C(A,B):                                 # sub class
##    def __init__(self):
##        super().__init__()
##        print("in C init")
##
##    def feat(self):
##        super().feature2()
##
##a1=C()
##a1.feature1()
##a1.feat()



## Operators Overload------------------>
##a=5
##b=5
##print(a+b)
##
##
##c='hello'
##d='world'
##print(c+d)
##
##
####e=5
####f='hello world'
####print(e+f)
##
##
##g="5"
##h="6"
##print(g+h)




##
##class student:
##    def __init__(self,m1,m2):
##        self.m1=m1
##        self.m2=m2
##
##    def __add__(self,other):
##        m1=self.m1+other.m1
##        m2=self.m2+other.m2
##        s3=student(m1,m2)
##        return s3
##
##    def __gt__(self,other):
##        s1=self.m1+self.m2
##        s2=other.m1+other.m2
##        if s1>s2:
##            return True
##        else:
##            return False
##    def __str__(self):
##        return self.m1,self.m2
##               
##       
##
##s1=student(58,69)
##s2=student(60,65)
##
##s3=s1+s2
##print(s3.m1)
##
##if s1>s2:
##    print("s1 wins")
##else:
##    print("s2 wins")
##
##
##print(s1.__str__())


"""
INFYTQ Questions
"""

##def student(firstname, degree="B.E.", sem="sixth"):
##    print(firstname + "is studying in " + sem + "semester" + degree)
##    
##student("john")
####student(qualification="B.sc.")
####student(firstname="mary")
####student()

##def bubble_sort(input_list):
##    num=len(input_list)
##    print(num)
##    for index1 in range (num):
##        for index2 in range (0, num-index1-1):
##            if input_list[index2] > input_list[index2+1]:
##                input_list[index2],input_list[index2+1] = input_list[index2+1] ,input_list[index2]
##        
##input_list=[4,10,2,7,1,8]



##def display_values(input1,input2):
##    for index in range (0,len(input1)):
##                        if input1[index]%input2==0:
##                            print(input1[index])
##                        
##                        
##display_values([3,4],2)
###display_values(1,2,"hello")
###display_values({5},"bye")
###display_values("bye",2)



##def function(input_list):
##    mid_pos=len(input_list)//2
##    low=0
##    high=len(input_list)-1
##    while(input_list[mid_pos]<input_list[low]):
##        low=low+2
##    if (low<=high):
##        temp=input_list[low]
##        input_list[low]=input_list[high]
##        input_list[high]=temp
##    return input_list
##list1=[39, 45, 22, 51, 62, 12, 6]
##sub_list1=function(list1[:5])
##print(sub_list1)


##def function(string,list1):
##    num=1
##    while num!=len(string)-1:
##        if (len(string)%2==0 or string[num] in ('a','b','c')):
##            list1.append(string[num-1])
##        num+=1
##        list1=function(string[num:],list1)
##        break
##    return list1
##print(function("Analytically",[]))


##class Shirt:
##    def __init__ (self):
##        self.colour="Red"
##        self.size="Medium"
##shirt1=Shirt()
##shirt2=shirt1
##shirt1.colour="Yellow"
##shirt2.colour="Green"
##shirt2=Shirt()
##shirt2.size="Large"




##
##def dict_items(dict1):
##    try:
##        dict2=[]
##        for key in dict1.keys():
##            dict2[key]=dict1[key]+key
##            dict1[key]=dict2[key+1]
##    except IndexError:
##       print("Index error occured")
##    except ValueError:
##       print("Value error occured")
##    finally:
##       print("Finally done")
##
##try:
##    dict_1({1:1,2:22,3:33})
##    print("Function call done")
##except KeyError:
##    print("Key Error occured")
##except:
##    print("Some error occured")

    
    
##s="GfG1"
##print(s.islower(),s.isupper(),s.isalpha(),s.isdigit())
##
##
##T=int(input())
##while T!=0:
##    S=str(input())
##    if ((S.isdigit()==False) and (S.isalpha()==False) and (S.isupper==False) and (S.islower==False)):
##        print("YES")
##    else:
##        print("NO")
##    T-=1 




##a=int(input())
##b=a//2
##c=0
##
##while (b!=0):
##    if b<a:
##        d=b*b
##        if d==a:
##            print("true")
##            break
##        else:
##            c+=d
##            if (c==a):
##                print("true")
##                break
##    else:
##        print("false")
##    b-=1           
    
    
    
        
    














      
