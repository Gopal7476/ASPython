##coll=input() #AEC ACET ACOE
##year=int(input())#4
##per=float(input()) #>=60
##bc=int(input()) #0
##branch=input() #CSE ECE IT
##gen=input() #F
##if(coll=='AEC' and year==4 and per>=60 and bc==0 and (branch=='CSE' or branch=='ECE' or branch=='IT') and gen=='F'):
##    print("u r eligible")
##else:
##    print('u r not eligible')





##coll=input()
##branch=input()
##per=float(input())
##bl=int(input())
##if (coll!='ACOE' and (branch!='MECH' or branch!='EEE' or branch!='CIVIL') and per>=65 and per<=80 and bl<=2):
##    print("u r eligible")
##else:
##    print("u r not eligible")




##
##def abc(coll,branch,per,bl):
##    if (coll!='ACOE' and (branch!='MECH' or branch!='EEE' or branch!='CIVIL') and per>=65 and per<=80 and bl<=2):
##          print("u r eligible")
##    else:
##          print("u r not eligible")
##
##
##coll=input()
##branch=input()
##per=float(input())
##bl=int(input())
##abc(coll,branch,per,bl)





##import chinnuinfytq as ci
##
##
##coll=input()
##branch=input()
##per=float(input())
##bl=int(input())
##
##d=ci.abc(coll,branch,per,bl)
##
##
##print(d)




### looping statement(for , while)
### for loop
##n=int(input())
##for i in range(0,n+1,1): #definite forward looping
##    print(i)
##for i in range(0,n+1,2): #definite forward looping
##    print(i)    
##for i in range(n,0,-1):    #definite backward looping
##    print(i)
##
##
###while loop
##n=int(input())
##i=1
##while i<=n: 
##    print(i)
##    i+=1
##
##
##
##def drive_check(per):
##    if per>65:
##        print("eligible")
##    else:
##        print("not eligible")
##
##t=int(input())                  #test cases
##for i in range(t):
##    per=int(input())
##    drive_check(per)
##
##
##
##def drive_check(per):
##    if per>65:
##        print("eligible")
##        return 1
##    else:
##        print("not eligible")
##        return 0
##
##
##while 1:
##    per=int(input())
##    c=drive_check(per)
##    if(c==0):
##        break
##
##
##def drive_check(per):
##    if per>65:
##        print("eligible")
##        return 1
##    else:
##        print("not eligible")
##        return 0
##
##c=1
##while c!=0:
##    per=int(input())
##    c=drive_check(per)
##
####
####
####T,n=map(int,input().split())  #multiple inputs 1-int 2-int , 1-float 2-float
####
####T,n=map(str,input().split())  #multiple inputs 1-int 2-char or float
####n=int(n)
####n=float(n)






##def abc(coll,branch,per,bl):
##        if (coll!='ACOE' and (branch!='MECH' or branch!='EEE' or branch!='CIVIL') and per>=65 and per<=80 and bl<=2):
##          print("u r eligible")
##        else:
##          print("u r not eligible")
##
##
##
##
##
##
##
##def drive(coll,branch,per,bl):
##        if (coll!='ACOE' and (branch!='MECH' or branch!='EEE' or branch!='CIVIL') and per>=65 and per<=80 and bl<=2):
##              return(1)
##        else:
##              return(0)





##### LAST YEAR INFYTQ QUESTIONS
##num1=5
##num2=4
##while(num2>=1):
##    print("*")
##    for index in range(1,num1+1):
##        print("*")
##        num2-=1
##    print('*')    
##
##
##
##
##
##
##def fun(var1,var2,var3):
##    if (var1<=var2):
##        if (var3>=var2):
##            if (var1+var2>var3):
##                print(-1)
##            else:
##                print(-2)
##        else:
##            if(var1+var3>var2):
##                print(-3)
##            else:
##                print(-4)
##fun(156,2100,9500)                





##def fun(name,no_of_seats=100,*marks):
##    pass
##fun("John",350,21)
##fun("John")
##fun("John",100,21,16)
##
##
##
##def fun(n):
##    if n==0:
##        return
##    print(n)
##    fun(n-1)
##    print(n)
##n=int(input())    
##fun(n)
##
##
##
##
##def fun(n):
##    if n==0:
##        return 1
##    return 1+fun(n-1)
##res=fun(10)
##print(res)
##
##
##
##
##def fun(n):
##    if n==0:
##        return 1
##    if n%2==0:
##        return 1+fun(n-2)
##    else:
##        return 1+fun(n-1)
##res=fun(10)
##print(res)



##def fun(n):
##    if n==0:
##        return 0
##    if n==1 or n==2:
##        return 1
##    else:
##        return (fun(n-1)+fun(n-2))
##f=fun(5)
##print(f)
##
##
##
##
##
##def my_fun(a,b):
##    if (a<=0 or b<=0):
##        return 1
##    return my_fun(a-2,b-1)+my_fun(a-3,b-2)
##a=my_fun(10,5)
##print(a)



### most afficient no's  74 77 90 100 for test the below code
##if per>=75 and per<=85:
##    sc=5000
##elif per>85 and per<=95:
##    sc=8000
##elif per>95:
##    sc=10000
##else:
##    sc=0




### OOPS CONCEPT------------------------->
##
##
##
###class:  is a collection of member var and member function(methods)
###object: instance of class 
###constructor: default method
##class HumanBeing:
##    pass
##
##hb1=HumanBeing() #creation of object
#in this code
#hb1 is object
#HumanBeing is class
##
##
##
##
##class HumanBeing():
##    def __init__(self):
##        print("Human Being")
##
##hb1=HumanBeing()  #creation ofobject
##
##
##
##
##class HumanBeing():
##    def __init__(self):
##        print("Human Being")
##    def display(self):
##        print("hai")      
##
##hb1=HumanBeing()
##hb1.display()
##
##
##
##
##
##class HumanBeing():
##    def __init__(self,n):
##        self.name=n #hb1.name="mahesh"
##    def display(self):
##        print(self.name)      
##
##hb1=HumanBeing("mahesh")
##hb1.display()
##
##
##
##class HumanBeing():
##    def __init__(self,n):
##        self.name=n #hb1.name="mahesh"
##    def display(self):
##        print(self.name)      
##
##hb1=HumanBeing("mahesh") #creation of object
##print(hb1.name) #accesing member variable
##hb1.display() #accessing member function
##
##
##
##
##
##
##class HumanBeing():
##    def __init__(self,n,phno,adhar):
##        self.name=n#hb1.name="mahesh"
##        self.phno=phno
##        self.adhar=adhar
##    def display(self):
##        print(self.name,self.phno,self.adhar)      
##
##hb1=HumanBeing("mahesh","9951722111","7894512")
##hb1.display()
##
###3 diff types of variable
###instance
###class
###static
###(local variable)-->ArithmeticError wrong




##class student:
##    college="ADITYA"  #class variable / insistance variable
##    def __init__(self,name,rollno,per):
##        self.name=name
##        self.rollno=rollno
##        self.per=per
##    def display(self):
##        print(self.name,self.rollno,self.per,student.college)
##
##std1=student("ravi",'123',65)
##std1.display()
##print(std1.name)
##
##
##
##class student:
##    college="ADITYA"
##    def __init__(self,name,rollno,per):
##        self.name=name
##        self.rollno=rollno
##        self.per=per
##    def display(self):
##        print(self.name,self.rollno,self.per,self.college)
##
##std1=student("ravi",'123',65)
##std1.display()
##
##
### we can access class variable with insistance variable
##
##
#####insistance method (code in above program)
##
##def __init__(self,name,rollno,per):
##        self.name=name
##        self.rollno=rollno
##        self.per=per
##def display(self):
##        print(self.name,self.rollno,self.per,student.college)
##
##
#####class method /static method
##
##
##class student:
##    college="ADITYA"
##    def __init__(self,name,rollno,per):
##        self.name=name
##        self.rollno=rollno
##        self.per=per
##    def display(self):
##        print(self.name,self.rollno,self.per,student.college)
##    @classmethod
##    def class_method(cls):
##        print("class method")
##
##std1=student("ravi",'123',65)
##std1.class_method()
##
##
##
##
##class hospital():
##    def __init__(self,name,area,phno):
##        self.name=name
##        self.area=area
##        self.phno=phno
##    def display(self):
##        print(self.name,self.area,self.phno)
##
##hos=hospital("ABC",'madapur, kakinada',"12345678910")
##hos.display()






##class student:
##    college="ADITYA"
##    def __init__(self,name,rollno,per):
##        self.name=name
##        self.rollno=rollno
##        self.per=per
##    def display(self):
##        print(self.name,self.rollno,self.per,student.college)
##    @classmethod
##    def m1(cls):
##        print("class method")
##
##    @classmethod
##    def class_method(cls):
##        print(cls.college)
##        cls.m1()
##
##    @staticmethod
##    def find_prime(n,a):
##        print(n,a)
##
##std1=student("ravi",'123',65)
##std1.class_method()
##std1.display()






###Inheritance:
###Single Inheritance:------------------------>
##class personal:
##    
##    def __init__(self,name,adhar,pan):
##        self.name=name
##        self.adhar=adhar
##        self.pan=pan
##    def display(self):
##        print(self.name,self.adhar,self.pan)
##
##class student(personal):
##    
##    def __init__(self,rollno,per,name,adhar,pan):
##        super().__init__(name,adhar,pan)
##        self.rollno=rollno
##        self.per=per
##        self.adhar="12345"
##        
##        
##    def display(self):
##        print(self.rollno,self.per,self.name,self.adhar,self.pan)
##
##
##std1=student(123,67,"raju","12345678910","hgb15ds")
##std1.display()







### Heriacal Inheritance:-------------------->
##class personal:
##    
##    def __init__(self,name,adhar,pan):
##        self.name=name
##        self.adhar=adhar
##        self.pan=pan
##    def display(self):
##        print(self.name,self.adhar,self.pan)
##
##class student(personal):
##    
##    def __init__(self,rollno,per,name,adhar,pan):
##        super().__init__(name,adhar,pan)
##        self.rollno=rollno
##        self.per=per
##        self.adhar="12345"
##        
##        
##    def display(self):
##        print(self.rollno,self.per,self.name,self.adhar,self.pan)
##
##class employee(personal):
##    def __init__(self,empid,salary,dept,name,adhar,pan):
##        self.empid=empid
##        self.salary=salary
##        self.dept=dept
##    def display(self):
##        print(self.empid,self.salary,self.dept)
##
##
##std1=student(123,67,"raju","12345678910","hgb15ds")
##std1.display()
##emp1=employee("2935","50K","cse","sudhir","12345","ertyj3456b")






### multi-level Inheritance:------------------>
##class telephone:
##    def __init__(self):
##        print("calls")
##
##
##class mobile(telephone):
##    def __init__(self):
##        super().__init__()
##        print("messages, basic games")
##
##class smartmobile(mobile):
##    def __init__(self):
##        super().__init__()
##        print("adv games, internet, movies")
##        
##sm1=mobile()



##class telephone:
##    def __init__(self):
##        print("calls")
##
##
##class mobile(telephone):
##    def __init__(self):
##        super().__init__()
##        print("messages, basic games")
##
##class smartmobile(mobile):
##    def __init__(self):
##        pass
##        
##sm1=smartmobile()







# multiple Inheritance:--------------->
##class acaresult:
##    def __init__(self,marks1,marks2):
##        self.sem1=marks1
##        self.sem2=marks2
##    def display(self):
##        print(self.sem1,self.sem2)
##        
##class sports:
##    def __init__(self,spname,noplayers,score):
##        self.spname=spname
##        self.noplayers=noplayers
##        self.score=score
##    def display(self):
##       print(self.spname,self.noplayers,self.score)
##       
##class personal(acaresult,sports):
##    pass
##
##p1=personal("cricket",11)
##p1.display()

"""------------------------------------------------------------><---------------------"""




##class demo:
##    college="ADITYA"
##    def __init__(self,name,course):
##        self.name=name
##        self.course=course
##        self.college="ACOE"
##    def display(self):
##        print(self.name,self.course,self.college)
##    @classmethod
##    def classmethod(cls):
##        print(cls.college)
##        print("hai")
##    @staticmethod   
##    def static():
##        print("HELLO")
##
##
##std1=demo("Ravi","B.Tech")
##std1.display()
##std1.classmethod()
##demo.classmethod()
##std1.static()
##demo.static()



##class demo:
##    college="ADITYA"
##    def __init__(self,name,course):
##        self.name=name
##        self.course=course
##        self.college="ACOE"
##class demo1(demo):
##        def display(self):
##            print(self.name,self.course,self.college)
##
##std1=demo1("Ravi","B.Tech")
##std1.display()
##
##
##
##
##class demo:
##    college="ADITYA"
##    def __init__(self,name,course):
##        self.name=name
##        self.course=course
##        self.college="ACOE"
##    def display(self):
##            print(self.name,self.course,self.college)   
##class demo1(demo):
##    pass
##       
##
##std1=demo1("Ravi","B.Tech")
##std1.display()



####vari and members about security
####private and public

##class demo:
##    college="ADITYA"
##    def __init__(self,name,course):
##        self.name=name
##        self.course=course
##        self.college="ACOE"
##class demo1(demo):
##        def display(self):
##            print(self.name,self.course,self.college)
##
##std1=demo1("Ravi","B.Tech")
##print(demo.college)  #public
##print(std1.college)  #public
##
##
##
##class demo:
##    college="ADITYA"
##    def __init__(self,name,course):
##        self.__name=name #private variable can give 2underscores
##        self.course=course
##        self.college="ACOE"
##class demo1(demo):
##        def display(self):
##            print(self.__name,self.course,self.college)
##
##std1=demo1("Ravi","B.Tech")
##std1.display()


####oops------->encapslation
##class demo:
##    college="ADITYA"
##    def __init__(self,name,course):
##        self.__name=name #private variable can give 2underscores
##        self.course=course
##        self.college="ACOE"
##    def get_name(self):
##        return self.__name
##class demo1(demo):
##        def __display_data(self):
##            name=super().get__name()
##            print(name,self.course,self.college)
##        def display(self):
##            self.__display_data()
##
##            
##std1=demo1("Ravi","B.TECH")
##std1.display()


###abstract--------------------------------------------------->
####for abstract can"t create object
##from abc import ABC,abstractmethod
##
##
##class demo(ABC):           #abstract class
##    @abstractmethod
##    def ab1(self):
##        print("HAI")
##    def ab2(self):
##        pass
##
##
##class sub1(demo):
##    def ab1(self):
##        print("HAI")
##    def ab2(self):
##        print("HAI")
##
##obj=sub1()



####DATA STRUCTURE------------------------------------------------------>

"""
DS--Topics for INFYTQ

binary search ----->Linear search: search all the index position
selection sort
insertion sort
bubble sort
hashing
stack
queue
linkedlist
"""


"""BINARY SEARCH & LINEAR SEARCH:----------->"""
##class search:
##    def __init__(self,data,key):
##        self.data=data
##        self.key=key
##    def linearsearch(self):
##        for i in range(len(self.data)):
##            if(self.key==self.data[i]):
##                print("Element Found")
##                break
##        else:
##            print("Element not found")
##    def binarysearch(self):
##         l=0
##         h=len(self.data)-1
##         ic=0
##         while(l<=h):
##             ic+=1
##             m=(l+h)//2
##             print(l,h,m)
##             print(self.data[l],self.data[h],self.data[m])
##             if (self.data[m]==self.key):
##                 print("Element Found")
##                 break
##             elif (self.data[m]<self.key):
##                 l=m+1
##             else:
##                 h=m-1
##         else:
##            print("Element Not Found")
##         print("Number Of Iteration =",ic)               
##obj=search([1,2,3,4,5,6,7,8,9],5)
##obj.linearsearch()
##obj.binarysearch()




"""
SELECTION SEARCH:---------------------->
I/P--: 11 7 12 14 19 1 6 18 8 16

O/P--:
pass1: 11 7 12 14 16 1 6 18 8 19
pass2: 11 7 12 14 16 1 6 8 18 19
pass3: 11 7 12 14 8 1 6 16 18 19
pass4: 11 7 12 6 8 1 14 16 18 19
pass5: 11 7 1 6 8 12 14 16 18 19
pass6: 8 7 1 6 11 12 14 16 18 19
pass7: 6 7 1 8 11 12 14 16 18 19
pass8: 6 1 7 8 11 12 14 16 18 19
pass9: 1 6 7 8 11 12 14 16 18 19
"""


##class sorting:
##    def __init__(self,data):
##        self.data=data
##    def selection_sort(self):
##        pass
##                       
##            
##    
##data=[11,7,12,14,19,1,6,18,8,16]
##obj=sorting(data)
##obj.selection_sort()




"""
STACK:------------------>
push,pop,overflow,underflow
display---> displays from top to bottom
"""


##class Stack:
##    def __init__(self,size):
##        self.size=size
##        self.top=-1
##        self.data=[-1 for _ in range(size)]
##    def push(self,val):
##        if self.top==self.size-1:
##            print("Stack Overflow")
##        else:
##            self.top=top+=1
##            self.data[self.top]=val
##    def pop(self,val):
##        if self.top==-1:
##            print("Stack under flow")
##        else:
##            self.data[self.top]=-1
##            self.top-=1
##            return val
##    def display(self):
##       if self.top==-1:
##           print("stack under flow")
##       else:
##           for i in range(self.top,-1,-1):
##               print(self.data[i])
##           
##
##    
##stack=Stack(6)
##stack.push(100)
##stack.push(1200)
##stack.push(1000)
##stack.push(500)
##stack.push(10)
##stack.push(30)
##stack.push(1100)
##stack.push(1050)
##stack.push(1)
##print(stack.pop(500))
##print("stack data")
##stack.display()




"""
QUEUE:------------>
insertion queue called as rear
deletion queue called as front
"""
##class Queue:
##    def __init__(self,size):
##        self.size=size
##        self.front=-1
##        self.rear=-1
##        self.data=[-1 for _ in range(size)]
##    def enqueue(self,val):
##        pass
##    def dequeue(self):
##        pass
##    def display(self):
##        pass
##
##            
##queue=Queue(6)        
    


"""
LINKED LISTS:----------------->
node: has data and adderess of next node
collection of nodes is called linked lists
"""
##class Node:
##    def __init__(self,val):
##        self.val=val
##        self.next=None
##
##
##class LinkedList:
##    def __init__(self):
##        self.head=None
##        self.tail=None
##
##    def addNode_end(self,val):
##        self.nnode=Node(val)
##        if self.head==None:
##            self.head=self.nnode
##            self.tail=self.nnode
##        else:
##            self.tail.next=self.nnode
##            self.tail=self.tail.next
##    def display(self):
##        temp=self.head
##        if(temp==None):
##            print(" No nodes")
##        else:
##            while(temp):
##                print(temp.val,end=" ")
##                temp=temp.next
##    def delete_end(self):
##        temp=self.head
##        if(temp==None):
##            print(" No nodes")
##        else:
##            while(temp.next.next):
##                temp=temp.next
##            temp.next=None
##            self.tail=temp
##    def delete_front(self):
##        temp=self.head
##        if(temp==None):
##            print(" No nodes")
##        else:
##            temp=temp.next
##            self.head.next=None
##            self.head=temp
##    def addNode_beg(self,val):
##        self.nnode=Node(val)
##        if self.head==None:
##            self.head=self.nnode
##            self.tail=self.nnode
##        else:
##            self.nnode.next=self.head
##            self.head=self.nnode
##    def addNode_pos(self,pos,val):
##        self.nnode=Node(val)
##        
##        if self.head==None:
##            self.head=self.nnode
##            self.tail=self.nnode
##        else:
##            if(pos==1):
##                self.addNode_beg(val)
##            else:
##                temp=self.head
##                i=1
##                while(i<pos-1 and temp):#1<3 
##                    temp=temp.next
##                    i+=1
##                if(temp):
##                    self.nnode.next=temp.next
##                    temp.next=self.nnode
##                else:
##                    print("Not in range")
##    def deleteNode_pos(self,pos):
##        temp=self.head
##        if(temp==None):
##            print(" No nodes")
##        else:
##            if(pos==1):
##                self.delete_front()
##            else:
##                i=1
##                while(i<pos-1 and temp):
##                    temp=temp.next
##                    i+=1
##                if(temp):
##                    temp.next=temp.next.next
##                else:
##                    print("not in range")
##                
##        
##        
##ll=LinkedList()
##ll.addNode_end(100)
##ll.addNode_end(200)
##ll.addNode_end(300)
##ll.addNode_end(400)
##ll.addNode_beg(500)
##ll.addNode_pos(1,700)
##ll.display()
##print()
##ll.deleteNode_pos(10)
##ll.display()


"""
Queue
"""
##class Queue:
##    def __init__(self,size):
##        self.size=size
##        self.front=-1
##        self.rear=-1
##        self.data=[]
##    def enqueue(self,val):
##        if self.rear==self.size-1:
##            print("Queue is FULL")
##        else:
##            if(self.rear==-1 and self.front==-1):
##                self.rear=0
##                self.front=0
##            else:
##                self.rear+=1
##            self.data.append(val)
##    def dequeue(self):
##        if self.front==-1 and self.rear==-1:
##            print("Queue is empty")
##        else:  
##            if(self.rear==self.front):
##                self.rear=-1
##                self.front=-1
##            else:
##                self.rear-=1
##            self.data.pop(0)
##            
##    def display(self):
##        if self.front==-1 and self.rear==-1:
##            print("Queue is empty")
##        else:
##            for i in range(self.front,self.rear+1):
##                print(self.data[i])
##queue=Queue(6)





##class Search:
##    def __init__(self,data,key):
##        self.data=data
##        self.key=key
##    def linearsearch(self):
##        for i in range(len(self.data)):
##            if(self.key==self.data[i]):
##                print("Element Found")
##                break
##        else:
##            print("Element is not Found")
##    def binarysearch(self):
##        l=0
##        h=len(self.data)-1
##        ic=0
##        while(l<=h):
##            ic+=1
##            m=(l+h)//2
##            if(self.data[m]==self.key):
##                print("Element is Found")
##                break
##            elif(self.data[m]<self.key):
##                l=m+1
##            else:
##                h=m-1
##        else:
##            print("Element Not found")
##        print(ic)
##                
##obj=Search([1,2,3,4,5,6,7,8,9],9)
##obj.binarysearch()








"""
ds:
binary search
selection sort
insertion sort
bubble sort
hashing
stack
queue
linkedlist

1 2 3 4 5 6 7 8 9 
"""





##class Sorting:
##    def __init__(self,data):
##        self.data=data
##    def selection_sort(self):
##        pas=0
##        for i in range(len(self.data)-1,0,-1):
##            pas+=1
##            me=i
##            for j in range(i-1,-1,-1):
##                if(self.data[me]<self.data[j]):
##                    me=j
##            temp=self.data[me]
##            self.data[me]=self.data[i]
##            self.data[i]=temp
##            print(pas,"-->",self.data)
##        #print(self.data)       
##    def insertion_sort(self):#23,11,32,43,12,45,87,54,67
##        pas=1
##        for i in range(1,len(self.data)):
##            ele=self.data[i]
##            for j in range(i-1,-1,-1):
##                if(ele<self.data[j]):#11<23
##                    self.data[j+1]=self.data[j]
##                else:
##                    self.data[j+1]=ele
##                    break
##            else:
##                self.data[0]=ele
##            print(pas,"-->",self.data)
##            pas+=1
##    def bubble_sort(self):
##        for i in range(len(self.data)):
##            sc=0
##            for j in range(len(self.data)-1):
##                if(self.data[j]>self.data[j+1]):
##                    sc+=1
##                    temp=self.data[j]
##                    self.data[j]=self.data[j+1]
##                    self.data[j+1]=temp
##            print(self.data,sc)
##            if(sc==0):
##                break
##        
##            
##            
##data=[23,11,32,43,12,45,87,54,67]
##obj=Sorting(data)
##obj.bubble_sort()
##
##
##
##
##
##
##
##
##"""
##pass1:   11 34 55 100 19 12 60 18 16 110   psc=5
##
##pass2:  11 34 55 19 12 60 18 16 100 110   psc=5
##
##pass3:  11 34 19 12 55 18 16 60 100 110   psc=4
##
##pass4:  11 19 12 34 18 16 55 60 100 110   psc=4
##
##pass5:  11 12 19 18 16 34 55 60 100 110   psc=3
##
##pass6:  11 12 18 16 19 34 55 60 100 110  psc=3
##
##pass7:  11 12 16 18 19 34 55 60 100 110  psc=1
##
##pass8:  11 12 16 18 19 34 55 60 100 110  psc=0 
##
##
##
##
##
##
##
##
##
##
##
##
##
##pass1:11 7 12 14 16 1 6 18 8 19
##
##pass2:11 7 12 14 16 1 6 8 18 19
##
##pass3:11 7 12 14 8 1 6 16 18 19
##
##pass4:11 7 12 6 8 1 14 16 18 19
##
##pass5:11 7 1 6 8 12 14 16 18 19
##
##pass6:8 7 1 6 11 12 14 16 18 19
##
##pass7:6 7 1 8 11 12 14 16 18 19
##
##pass8:6 1 7 8 11 12 14 16 18 19
##
##pass9:1 6 7 8 11 12 14 16 18 19
##
##
##34 55 32 65 22 43 54 12 11
##
##pass1: 34 55 32 11 22 43 54 12 65
##
##pass2: 34 12 32 11 22 43 54 55 65
##
##oo;'
## 
##
##pass4: 34 12 32 11 22 43 54 55 65
##
##pass5: 22 12 32 11 34 43 54 55 65
##
##pass6: 22 12 11 32 34 43 54 55 65
##
##pass7: 11 12 22 32 34 43 54 55 65
##
##"""



##class Sorting:
##    def __init__(self,data):
##        self.data=data
##    def selection_sort(self):
##        pas=0
##        for i in range(len(self.data)-1,-1,-1):
##            pas+=1
##            me=i
##            for j in range(i-1,-1,-1):
##                if(self.data[me]<self.data[j]):
##                    me=j
##            temp=self.data[me]
##            self.data[me]=self.data[i]
##            self.data[i]=temp
##            print(pas,"-->",self.data)
##        #print(self.data)
##
##
##    
##data=[11,7,12,14,19,1,6,18,8,16]
##obj=Sorting(data)
##obj.selection_sort()
##
##
##
##
##
##
##
##
##"""
##11 7 12 14 19 1 6 18 8 16
##
##
##pass1:11 7 12 14 16 1 6 18 8 19
##
##pass2:11 7 12 14 16 1 6 8 18 19
##
##pass3:11 7 12 14 8 1 6 16 18 19
##
##pass4:11 7 12 6 8 1 14 16 18 19
##
##pass5:11 7 1 6 8 12 14 16 18 19
##
##pass6:8 7 1 6 11 12 14 16 18 19
##
##pass7:6 7 1 8 11 12 14 16 18 19
##
##pass8:6 1 7 8 11 12 14 16 18 19
##
##pass9:1 6 7 8 11 12 14 16 18 19
##
##"""
##
##
##
##class Stack:
##    def __init__(self,size):
##        self.size=size
##        self.top=-1
##        self.data=[-1 for _ in range(size)]
##    def push(self,val):#top-1
##        if self.top==self.size-1:#-1==5
##            print("Stack Overflow")
##        else:
##            self.top+=1#0
##            self.data[self.top]=val# 100 -1 -1 -1 -1 -1
##            
##    def pop(self):
##        if self.top==-1:
##            print("stack Under flow")
##        else:
##            val=self.data[self.top]
##            self.data[self.top]=-1
##            self.top-=1
##            return val
##    def display(self):
##        if self.top==-1:
##            print("stack Under flow")
##        else:
##            for i in range(self.top,-1,-1):
##                print(self.data[i])
##        
##    
##stack=Stack(6)
##stack.push(100)
##stack.push(200)
##stack.push(400)
##stack.push(300)
##stack.push(600)
##stack.push(1000)
##stack.push(20)
##print(stack.pop())
##print(stack.pop())
##print(stack.pop())
##print(stack.pop())



