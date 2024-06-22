# print("Hello World")
# name="Abhinav"
# id=1001
# rollno=False
# account=15.5
# name2=name
# address=None

# print(name2)
# print(type(address))
# print(type(name))
# print(type(rollno))
# print(type(account))
# print(type(id))

# a=5
# b=70
# sum=a+b
# print("Sum of", a, "and", b ,"=",sum)

# a=int(input("Enter First Value :"))
# b=float(input("Enter Second Value :"))
# sum=a+b
# print(sum)

# a=int(input("Enter First Value :"))
# b=int(input("Enter Second Value :"))
# sum=a+b
# print(sum)

# a="My Name Is Abhinav"
# print(len(a))
# print(a[0])
# print(a[1:4])
# name=input("Enter Your Name :")

# print(len(name))
# print(type(name))

# b="sdn$ dfkd $ dfjdk $ lkdjf $$kdf $$"
# # print(b.count("$"))

# a=input("Enter Value of A :")
# b=input("Enter Value of B :")
# c=input("Enter Value of C :")
# d=input("Enter Value of D :")
# e=input("Enter Value of E :")

# if(a>=b and a>=c and a>=d and a>=e):
#     print("A is Largest Nubmer",a)
# elif(b>=c and b>=d and b>=e):
#     print("B is Largest",b)
# elif(c>=d and a>=e):
#     print("C is Largest Number",c)
# elif(d>=e):
#     print("D is Largest Number",d)
# else:
#     print("E is Largest Number",e)        

# age=int(input("Enter You Age :"))

# if(age>=18):
#     if(age>=80):
#         print("You can't Drive")
#     else:
#         print("You Can Drive")    
# else:
#     print("You Can't Drive")        

# marks=[1,5,8,2,7,6,2]

# marks.insert(2,7)
# print(marks)

# a=input("Enter First Name :")
# b=input("Enter Second Name :")
# c=input("Enter Third Name :")

# name=[]
# name.append(a)
# name.append(b)
# name.append(c)
# print(name)

# obj={
#     "name":"Abhinav",
#     "class":"MCA",
#     "Rollno":"222608",
#     "subject":{
#         "MobileApplication":45,
#         "Java":55,
#         "Php":58
#     }
# }

# obj["name"]="Garima"
# obj["bf"]="Abhinav"
# print(obj)

# while True:
#     print("Hello World")

# count=5
# while count<6:
#     print(count)
#     count-=1

# i=100
# while i>=1:
#     print(i)
#     i-=1

# n=int(input("Enter the Number :"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# num=[4,8,84,75,787,84,9,78,48,4]
# i=0

# while i<len(num):
#     if(num[i]==9):
#         print("Found index no :", i)
#     i += 1\

# i=0

# while i<=5:
#     if i ==3:
#         i += 1
#         continue
#     print(i)
#     i += 1

# a=int("5")
# b=1.5
# sum=a+b
# print(sum)

# a=["Abhinav","Kriti","Yash"]
# i=0
# while i<=len(a):
#     print(a[i])
#     i += 1

# a=(1,"a",5)
# print(a)

# a=[1,2,5,4,2,8,2]
# a.remove(5)
# print(a)

# a=(1,485,84,548,45,1,1)


# print(a.index(84))

# obj={
#     "name":"Abhinav",
#     "Class":"MCA",
#     "Subject":["Maths","Science"]
# }
# print(obj.values)

# a=[1,2,1,2,1]
# b=a.copy()
# b.reverse()
# print(b)

# for i in range(2,22,2):
#     print(i)

# a=int(input("Enter the Number :"))
# for i in range(1,11):
#     print(i * a)

# i=0
# while i<=len(a):
#     print(a[i])
#     i += 1
# i=0

# while i<=10:
#     print(i)
#     i += 1

# a=[1,2,5,2,85,92,81,48]
# i=0
# while i<=len(a):
#     print(a[i])
#     i += 1

# a="Hey My Name is Abhinav"
# idx=0
# while idx<=len(a):
#         print(a[idx])
#         idx += 1
# a=int(input("Enter number :"))

# for i in range(1,11):
#     print(a * i)
# name=["Abhinav","Shobhit","Yash","Kriti"]

# def print_list(list):
#   print(len(list))

# print_list(name)

# number=int(input("Enter the Number :"))

# def print_no(a):
#     if a%2 ==0:
#         print("Even Number")
#     else:
#         print("Odd Number")


# print_no(number)    

# def show(a):
#     if(a == 0):
#         return
#     print(a)
#     show(a-1)

   
# show(10)   

# number=int(input("Enter Number :"))

# def show():
#     if number%2==0:
#         print(number,"is a Even Number")
#     else:
#         print(number,"is a Odd Number")

# show()    

# a="Enter You Number"
# i=0

# while i<=len(a):
#     print(a[i])
#     i += 1

# for i in a:
#     print(i)

# number=int(input("Enter Your Number :"))

# for i in range(1,11):
#     print(number*i)

# f=open("name.txt","r")
# data=f.read()
# print(data)

# f=open("name.txt","r")
# data=f.readline()
# data2=f.readline()
# print(data)
# print(data2)

# f=open("name.txt","a")
# data=f.write("\nI am fine")
# f.close()

# f=open("name.txt","r")
# data=f.read()
# print(data)
# f.close()

# f=open("name.txt","a")
# f.write("\nHow Are You")
# f.close()

# f=open("name.txt","w+")
# f.write("Kriti")
# print(f.read())

# f=open("name.txt","r+")
# f.write("Abhinav")
# print(f.read())
# f.close()

# number=int(input("Enter the Number :"))

# if number%2 == 0:
#     print(number,"is a Even Number")
# else:
#     print(number,"is a Odd number")

# star="*"
# idx=5
# for i in len(idx):
#     print(i)

# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print("*", end=' ')
#     print()

# for i in range(1,6):
#     print("*",end=" ")
# print()    

# n=5
# for i in range(1,6):
#     for j in range( i + 1):
#         print("*",end=" ")
#     print()    

# number=int(input("Enter Number :"))

# for i in range(1,11):
#     print(number * i)

# age=int(input("Enter You age :"))

# if age<=18:
#     print("Don't Drive")
# elif age>=18:
#     if age>=65:
#         print("Don't Drive")
#     else:
#         print("Drive")
# else:
#     print("Invaild Number")

# f=open("name.txt","a+")
# f.write("Kriti\n")
# print(f.read())

# with open("name.txt","w+") as f:
#     f.write("Kriti")
#     print(f.read())
# import os
# os.remove("name.txt")

# f=open("name.txt","w")
# f.write("Kriti")
# f.close()

# with open("name.txt","w") as f:
#     data=f.write()
#     print(data.replace("Kriti","Abhinav"))

# with open("name.txt","w") as f:
#     f.write("Hey My name is Abhinav\n")
#     f.write("I am From Rothak\n")
#     f.write("I complete my graduation in Bachelor Of Computer Application")

# with open("name.txt","r") as f:
#     data=f.read()    
#     print(data)

# newdata=data.replace("Abhinav","Kriti")
# print(newdata)    

# with open("name.txt","w") as f:
#     f.write(newdata)


# import os

# os.remove("name.txt")

# a=int(input("Enter the Number :"))
# b=int(input("Enter second Number :"))
# c=int(input("Enter Third Number :"))
# d=int(input("Énter Forth NUmber :"))
# e=int(input("Enter Fifth Number :"))

# if a>=b and a>=c and a>=d and a>=e:
#     print(a,"is largest number")
# elif b>=c and b>=d and b>=e :
#     print(b,"is largest number")
# elif c>=d and c>=e:
#     print(c,"is largest number")
# else:
#     print(e,"is largest number")     

# f=open("name.txt","w")
# f.write("hey my name is Abhinav")
# f.close()

# f=open("name.txt","r")
# data=f.read()
# print(data)

# newdata=data.replace("Abhinav","Kriti")

# f=open("name.txt","w")
# f.write(newdata)

# f=open("name.txt","r")
# print(f.read())

# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()    

# class student:
#     name="Abhinav"
#     rollno= 20

# a=student()    
# print(a.name,a.rollno)

# b=student()
# print(b.name,b.rollno)

# class student:
#     name="Abhinav"
#     rollno="52"
#     address="rohtak"

# a=student()
# print(a.name,a.rollno,a.address)    

# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#         print("adding new student on database")

# a=student("Kriti","10")
# print(a.name,a.rollno)  
# b=student("Abhinav","11")
# print(b.name,b.rollno)

# a="Abhinav"
# print(a)

# a=10
# b=10.5
# sum=a+b
# print(sum)

# a=int("10")
# b=2.5
# sum=a+b
# print(sum)

# age=int(input("Enter Your Age :"))

# if age >= 18:
#     if age >= 80:
#         print("Your age is",age,"You are too old")
#     else:
#         print("Your age is",age,"You can drive")
# elif age <= 18:
#             print("Your age is",age,"You can't drive") 
# else:
#         print("Invaild input")

# a=int(input("Enter the value of A :"))
# b=int(input("Enter the value of B :"))
# c=int(input("Enter the value of C :"))
# d=int(input("Enter the value of D :"))
# e=int(input("Enter the value of E :"))

# if a>=b and a>=c and a>=d and a>=e:
#     print(a,"is greatest number")
# elif b>=c and b>=d and b>=e:
#     print(b,"is greatest number")
# elif c>=d and c>=e:
#     print(c,"is greatest number")
# elif d>=e:
#     print(d,"is grestest number")
# else:
#     print(e,"is greatest number")        

# name="Abhinav"
# i=0
# while i <= len(name):
#     print(name[i])
#     i+=1 

# a=100

# while a>=0:
#     print(a)
#     a-=1


# for i in range(5):
#     for i in range(i+1):
#         print("*",end=" ")
#     print()

# a=open("name.txt","+w")
# a.write("Kriti")
# print(a.read())
# a.close()

# a=open("name.txt","a")
# data=a.write("Hello Kriti")
# print(data)
# a.close()

# with open("name.txt","r") as f:
#     print(f.read())

# import os
# os.remove("name.txt")    

# a={
#     "name":"Abhinav",
#     "friend":"Kriti"
# }
# b=a.copy()

# print(b)

# class student:
#     name="Abhinav"
#     rollno=10

# a=student()
# print(a.rollno)    

# class student:
#     @
#     def num(name):
#         name=name
#         print(name)

# a=student()
# print(a.num("Abhinav"))        

# a=int(input("Enter number :"))

# if a%2==0:
#     print(a,"is even number")
# else:
#     print(a,"is odd number")
# num=int(input("Enter the Number :"))

# for i in range(1,11):
#     print(num*i)

# number=[1,2,1,5,1]
# b=number.copy()
# b.reverse()
# print(b)

# a=[1,1,2,5,"abhi",4,5,5,8,5]
# b=[]

# for elm in a:
#     if a.count(elm)>1 and elm not in b:
#         b.append(elm)

# print(b)        

# a=[1,2,85,4,50,4,12,1,2]
# b=[]
# for i in a:
#     if a.count(i) >1 and i not in b:
#         b.append(i)

# print(b)
        
# def commanstr():
#     str1=input("Enter First String :")
#     str2=input("Enter Second String :")
#     s1=set(str1)
#     s2=set(str2)
#     lst=s1 & s2
#     print(lst)

# commanstr()    

# def commanfun():
#     str1=input("Enter the value : ")
#     str2=input("Enter the value : ")
#     s1=set(str1)
#     s2=set(str2)
#     lst=s1 & s2
#     print(lst)
    

# commanfun()    

# str1="Sheena loves eating apple and mango.Her sister also loves eating apple and mango"
# li=str1.split()
# print(li)

# for i in str1:
#     pass

# def commomword():
#     str1=input("Enter the name :")
#     str2=input("Enter the name :")
#     s1=set(str1)
#     s2=set(str2)
#     lst=s1 & s2
#     print(lst)

# commomword()    


# a=[1,2,85,4,50,4,12,1,2]
# b=[]
# for i in a:
#     if a.count(i) >1 and i not in b:
#         b.append(i)

# print(b)

# n=[1,1,2,5,2,1,2,5,2]
# lst=[]
# for i in n:
#     if n.count(i) >1 and i not in lst:
#         lst.append(i)

# print(lst)        

# a=int(input("Enter first number :"))
# b=int(input("Enter second number :"))
# sum=input("Enter second number :")

# def calc():
#     if sum == "-":
#         print(a ,"-",b,"=",a-b)
#     elif sum == "+":
#         print(a ,"+",b,"=",a+b)
#     elif sum=="*":
#         print(a ,"*",b,"=",a*b)
#     elif sum=="/":
#         print(a ,"/",b,"=",a/b)
#     elif sum =="%":
#         print(a ,"%",b,"=",a%b)
#     else:
#         print("Invaild Number")


# calc()       

# x=int(input("Enter number :"))

# match x:
#     case 0:
#         print(x,"is zero")
#     case 4:
#         print(x,"is four")
#     case _ if x==10:
#         print(x,"is ten")
#     case _ if x!=20:
#         print(x,"is not 80")
#     case _:
#         print(x)        

# name=["apple","banana","mango","lichi","watermallon"]

# for i in name:
#     print(i)
#     for j in i:
#         print(j)


# a="My name is {1} and i am from {0}"
# name="Abhinav"
# city="Rohtak"

# print(a.format(city,name))

# name="Abhinav"
# city="Rohtak"
# a=f"My name is {name} and i am from {city}"
# print(a)

# def add(a,b):
#     sum=a+b
#     print(sum)

# add(10,20)   

# a=5
# b=5
# sum=a+b
# print(sum)

# def recur(n):
#     if n==0 or n==0:
#         return 1
#     else:
#         return  n + recur(n-1)

# print(recur(5))

# class add:
#     name="Abhinav"

# a=add()    

# print(a.name)

# class sub:
#     def add(self,name):
#         self.name=name
#         print(name)

# a=sub()
# print(a.add("abhinav"))        

# def add(a,b):
#     ''' hey how are you'''
#     sum=a+b
#     print(sum)

# add(10,50)
# print(add.__doc__) 
   
# a="Hey my name is {1} and i am from {0}"
# name="Abhinav"
# city="Rohtak"

# print(a.format(name,city))
# name="Abhinav"
# city="Rohtak"
# a=f"Hey my name is {name} and i am from {city}"
# print(a)

# countries=("India","USA","England","Austalia","Scotland")
# print(countries)
# lst=list(countries)
# lst.append("Shrilanka")
# lst.pop(4)
# countries=tuple(lst)
# print(countries)

# a=int(input("Enter the number between 5 or 10 :"))

# if(a<=5 or a>=9):
#     raise ValueError("Érror")


# try:
#     number=int(input("Énter Number :"))
#     for i in range(1,11):
#         print(f"{number} X {i} = {number*i}")
# except Exception as e:
#     print(e)


# number=int(input("Enter first number :"))

# if(number<=5 or number>=9):
#     raise ValueError("Error")
# else:
#     print(number)

# name="Abhinav"
# city="Rohtak"
# a=f"My name is {name} and i am from {city}"
# print(a)

# def sum(a,b):
#     """This function is made for addition of two numbers"""
#     print(a+b)

# sum(4,5) 
# print(sum.__doc__)   

# a=335
# b=3352
# print("A") if a>b else print("=") if a==b else print("B")

# a=100
# b=10
# print("A") if a>b else print("=") if a==b else print("B")

# marks=[1,2,5,7,5,85,54,5,45,55]

# for index,mark in enumerate(marks,start=1):
#     print(mark)
#     if(index==5):
#         print("Awesome Abhinav")       

# import python2

# python2.welcome()
# python2.sum()

# from python2 import welcome as w

# w()

# import os

# os.remove("__pycache__")

# f=open("python2.py","w")
# f.write()

# import python2

# python2.welcome()
# print(python2.a)

# import python2

# python2.welcome()

# name="Abhinav"
# city="Rohtak"
# a=f"My name is {name} and i am from {city}"
# print(a)

# def sum(a,b):
#     """Hey this function is Use for Addition of two numbers"""
#     print(a+b)

# sum(20,50)
# print(sum.__doc__)    

# marks=[10,25,45,4,2,45,8,52,21]

# for index,a in enumerate(marks,start=1):
#     print(a)
#     if(index==4):
#         print("Same on you")

#   def recur(n):
#     if n==0 or n==0:
#         return 1
#     else:
#         return  n + recur(n-1)

# print(recur(5))
  



# def rec(num):
#     if(num==0 or num==1):
#         return 1
#     else:
#         return num + rec(num-1)

# print(rec(5))

# try:
#     num=int(input("Enter first number :"))
#     for i in range(1,11):
#         print(num*i)
# except Exception as e:
#     print(e)        

# num=int(input("Enter number :"))

# if(num<=5 or num>=9):
#     raise ValueError("Invaild number")
# else:
#     print(num)

# x=int(input("Enter number :"))

# match x:
#     case 0:
#         print(x,"is zero")
#     case 4:
#         print(x,"is four")
#     case _ if x==10:
#         print(x,"is ten")
#     case _ if x!=20:
#         print(x,"is not 80")
#     case _:
#         print(x)  

# x=int(input("Enter number :"))

# match x:
#     case 0:
#         print(x,"is 0")
#     case 4:
#         print(x,"is 4")
#     case _ if x == 10:
#         print(x,"is equal 10")
#     case _ if x !=20:
#         print(x,"is not = 20")
#     case _:
#         print(x)            

# import python2

# python2.welcome()

# a=5
# b=12

# print("A")if a>b else print("=") if a==b else print("B") if a<b else print("invaild number")

# import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# if(not os.path.exists("data/Day")):
#     for i in range(1,101):
#         os.mkdir(f"data/Day{i}")

# import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# os.rename("classes","Python playlist")

# if(not os.path.exists(f"data/Day{1}")):
#     for i in range(1,101):
#         os.rename(f"data/Day{i}",f"data/Tutorial {i}")    



# os.rename("data","Python Playlist")

# for i in range(1,101):
#     os.rename(f"Python Playlist/Tutoria {i}",f"Python Playlist/Tutorial {i}")    


# folder= os.listdir("Python Playlist")

# for i in folder:
#     print(i)
#     print(os.listdir(f"Python Playlist/{i}"))



# if(not os.path.exists("Python playlist")):
#     os.mkdir("Python playlist")

# for i in range(1,101):
#     os.rename(f"Python playlist/Tutorial {i}",f"Python playlist/Day {i}")    

# folder=os.listdir("Python playlist")
# print(folder)

# for i in folder:
#     print(i)
#     print(os.listdir(f"Python playlist/{i}"))

# a=42

# def sum():
#     global a
#     a=55
#     b=50
#     print(b)

# sum()    
# print(a)

# import python2

# python2.welcome()

# import os

# if(not os.path.exists("Python playlist")):
#     os.mkdir("Python playlist")

# for i in range(1,101):
#     os.mkdir(f"Python playlist/Tutorial {i}")    

# with open("python2.txt","r") as f:
#     f.seek(10)
#     print(f.tell())
#     data=f.read(5)
#     print(data)

# def sum(a):
#     print(a*5)

# sum =lambda a: a*5

# print(sum(2))    

# sum=lambda a:a+5

# print(sum(55))

# sum=lambda a,b:(a+b)/2

# print(sum(50,10))

# def add(a):
#     return a+1

# a=[1,2,3,4,5,6,7]
# newlist=list(map(add,a))  

# print(newlist)

# a=[1,2,3]
# b=[1,2,3]

# print(a is b)
# print(a == b)

# a=154
# b=15

# print(a) if a>b else print("=") if a==b else print(b)

# a=[1,2,1,2,5,4,8,5,6,44,5,88,54]

# for index,i in enumerate(a):
#     if(index==9):
#         print("Congrulations",i)
#     else:
#         print(i) 
    

# with open("text.py","w") as f:
#     f.write("Hello")

# import os

# os.remove("text.py")

# a=5

# def sum():
#     global a
#     a=10
#     return a


# c=sum()
# print(c)
# print(a)

# sum=lambda a,b:a+b

# print(sum(10,20))


# class obj:
#     name="Abhinav"
#     occupation="Web Developer"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a=obj()
# a.info()  

# b=obj()
# b.name="Garima"
# b.occupation="Backend Developer"

# b.info()

# def greet(a):
#     def mzx():
#         print("Good Morning")
#         a()
#         print("Thanks For Visit")
#     return mzx
    

# @greet
# def hello():
#     print("Hello World")

# hello()

# class obj:
#     def __init__(self,name,role):
#         self.name=name
#         self.role=role

#     @property
#     def info(self):
#         print(f"My name is {self.name} and i am a {self.role}")    

# a=obj("Abhinav","Web Developer")
# a.info        
# b=obj("Garima","Backend Developer")
# b.info

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello Abhinav How are u what are you doing right now and don't lie another wise i tell your dad")
# engine.runAndWait()

# def sum():
#     """This function is use for add two numbers"""
#     print(10+10)

# sum() 
# print(sum.__doc__)   

# sum=lambda a,b:a+b
# print(sum(10,50))

# a=151
# b=15

# print("A")if a>b else print("=") if a==b else print("B")

# a={1,5,2,54,52,}
# b={12,5,2,55,21,23}
# c=a.union(b)
# print(type(a),a)

# print(1=="1")

# n=5
# for i in range(1,6):
#     for j in range( i + 1):
#         print("*",end=" ")
#     print()  

# for i in range(1,6):
#     for j in range(i + 1):
#         print("*",end=" ")
#     print()

# list=["Abhinav","Garima","Kriti","Sweata","Priya","Tanvi"]

# name=input("Enter your name :")

# if(name in list):
#     print(f"Abhinav i think u know {name}")
# else:
#     print("Unknown")    



# for i in range(0,6):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()    

# i=1
# num=int(input("Enter your Number :"))
# while(i<=num):
#         print("Hello")
#         i +=1

# a="Hey Abhinav"
# i=0
# while(i<=len(a)):
#     print(a[i])
#     i += 1

# try:
#     no=int(input("Enter number :"))

#     for i in range(1,11):
#         print(no*i)
# except:
#     print("Invaild number")     
# num=int(input("Enter number :"))

# if(num<=5 or num>=9):
#     raise ValueError("Invaild number")
# else:
#     print(num)


# a=int(input("Enter Number :"))

# if(a<=5 or a>=10):
#     raise ValueError("Invaild")
# else:
#     print(a)

# a=10
# b=10

# print("A") if a>b else print("=") if a==b else print("B")

# class sum:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     @property
#     def info(self):
#         print(f"Hey i am {self.name} and {self.id}")    

# a=sum("Garima",101)
# print(a.name)  
# b=sum("Abhinav",222608)
# print(b.info)  

# sum=lambda a,b:print(a+b)

# sum(55,55)

# import os

# for i in range(1,101):
#     os.mkdir(f"Python Tutorial/Tutorial {i}")

# a=int(input("Enter the number :"))

# for i in range(1,a+1):
#     print("*"*i,end="")
#     print("")

# a=int(input("Enter the number :"))

# for i in range(1,a+1):
#     print("*"*i,end="")
#     print("")

# a=int(input("Enter the number :"))

# for i in range(1,11):
#     print(f"{a} x {11-i}={a*(11-i)}")

# def avg(a,b):
#     avarage=100*(a+b)/500
#     print(avarage)
#     return avarage

# a=avg(164,200)  
# print(a)  

# def fac(a):
#     if(a==1 or a==0):
#         return 1
#     else:
#         return a*fac(a-1)
    
# print(f"The factorial of this number is {fac(1)}")    

# num=int(input("Enter the number :"))

# for i in range(0,num+1):
#     print("*"*(6-i),end="")
#     print("")

# computer=1
# list={
#     "s":1,
#     "p":0,
#     "c":-1
# }
# list2={
#     1:"Stone",
#     0:"Paper",
#     -1:"Syzer"
# }
# youstr=input("Enter your choice :")
# you=list[youstr]

# print(f"You choose {list2[you]} and computer choose {list2[computer]}")

# if(computer==you):
#     print("Draw try again")
# else:
#     if(computer==1 and you==0):
#         print("You win")
#     elif(computer==1 and you==-1):
#         print("You lose")
#     elif(computer==0 and you==1):
#         print("you lose")
#     elif(computer==0 and you==-1):
#         print("You Win")
#     elif(computer==-1 and you==0):
#         print("You lose")
#     elif(computer==-1 and you==1):
#         print("You Win")
#     else:
#         print("Something went wrong")                            

# a=[1,1,2,5,2,5,12,55,55,55]
# b=set(a)
# print(list(b))

# def table(a):
#     tbl=""
#     for i in range(1,11):
#         tbl += f"{a} x {i} = {a*i}\n"
#         with open(f"table/table {a}.txt","w") as f:
#             f.write(tbl)

# for i in range(2,21):
#     table(i)

# for i in range(1,11):
#     print("*"*i,end="")
#     print()

# list=[]
# name=input("Enter the number :")

# list.append(name)
    

# print(list)

# for i in range(1,6):
#     print("*"*(6-i),end="")
#     print()

# import os

# for i in range(1,101):
#     os.mkdir(f"Python Tutorial/Tutorial {i}")

# def table(a):
#     tbl = ""
#     for i in range(1,11):
#         tbl += f"{a} x {i} = {a*i}"
#         with open(f"tables/table {a}.txt","w") as f:
#             f.write(tbl)    

# for i in range(2,20):
#     table(i)

# def table(a):
#     tbl=""
#     for i in range(1,11):
#         tbl += f"{a} x {i} = {a*i}\n"
#         with open(f"tables/table{a}.txt","w") as x:
#             x.write(tbl)

# for i in range(2,21):
#     table(i)    
# import os
# os.mkdir("tables")


# def table(a):
#     tbl=""
#     for i in range(1,11):
#         tbl += f"{a} x {i} = {a*i}\n"
#         with open(f"tables/table {a}.txt","w") as f:
#             f.write(tbl)

# for i in range(1,20):
#     table(i)

# for i in range(1,11):
#     print("*"*(11-i),end=" ")
#     print("")

# n=5
# for i in range(1,6):
#     for j in range( i + 1):
#         print("*",end=" ")
#     print()  

# for i in range(0,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(0,6):
#     print("*"*i,end=" ")
#     print("")

# for i in range(0,6):
#     for j in range(i):
#         print("*",end=" ")
#     print("")    

# class obj:
#     name="Abhinav"  #class attribute
#     friend="Garima"
    
#     @property
#     def info(self):
#         print(f"Hey {self.name} {self.friend} is your gf")

# a=obj()
# a.name="Sunny" # int attribute
# a.info
# print(a.name)    

# sum=lambda *x:for i in 

# sum(1,2,3,4,5,6,7,8,9,1,2,3)

# a=5
# b=5

# print("A") if a>b else print("=") if a==b else print("b")

# list=["Abhinav","Garima","Tanvi","Ishu"]
# name=input("Enter your name :")

# if(name in list):
#     print(f"Abhinav {name} is your gf")
# else:
#     print("invaild")

# def greet(a):
#     def mzx():
#         print("Good Morning")
#         a()
#         print("Thanks For Visit")
#     return mzx
    

# def greet(xy):
#     def mx():
#         print("Good morning")
#         xy()
#         print("Good night")
#     return mx


# @greet
# def name():
#     print("Hello World")

# name() 

# class obj:
#     def __init__(self):
#         print("Hello")   

# a=obj()        `

# class obj:
#     company="Microsoft"
#     def __init__(self,name,salary,pin):
#         self.name=name
#         self.salary=salary
#         self.pin=pin

# a=obj("Abhinav","15k","124001")
# print(a.name,a.salary,a.pin)        

# class obj:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         print(f"The name of employe is {self.name} and salary is {self.salary}")


# class newobj(obj):
#     def sum(self):
#         print(self.name)
#         print(self.salary)


# a=obj("Abhinav","789545")   
# b=newobj("Garima","789654")

# b.sum()

# class emp:
#     name="Abhinav"
#     def show(self):
#         print(f"The name of employee is {self.name}")

# class emp2:
#     salary="78282"
#     def printshow2(self):
#         print(f"salary is {self.salary}")

# class coder(emp,emp2):
#     def printshow(self):
#         print(f"Thne name of employee is {self.name} and salary {self.salary}")


# # a=emp()
# # a.show()
# a=coder()
# a.printshow()
# a.show()   
# a.printshow2()     

# class parent:
#     def __init__(self):
#         self.a=[1,2,3,4,5,6]
#         print("Parent class")

# class child(parent):
#     def __init__(self):
#             print("Child class")

#     def show(self):
#         print(self.a)        

# class child2(child):
#     def __init__(self):
#             print("Child2 class")

#     def show2(self):
#         print(self.a)

# a=child()
# a.show()         

# class obj:
#     a=5
#     @classmethod
#     def show(self):
#         print(f"The value of a is {self.a}")

# b=obj()
# b.a=45 #instance attribute
# b.show()

# class obj:
#     a=5
#     def show(self):
#         print(f"The value of a is {self.a}")

# b=obj()
# b.a=45 #instance attribute
# b.name="Abhinav"
# b.show()
# print(b.name)
# c=obj()
# print(c.name)

# for i in range(1,6):
#     print("*"*(6-i),end="")
#     print("")

# for i in range(1,6):
#     for j in range((6-i)):
#         print("*",end=" ")
#     print("")   

# try:
#     a= int(input("Enter the value :")) 
#     b=int(input("Enter the second value :"))
#     print(sum=a+b)
# except:
#     print("Invaild number")   

# a=int(input("Enter the number :"))

# if (a<5 or a>10):
#     raise ValueError("Invalid")
# else:
#     print(a)

# l=[]
# for i in range(1,18):
#     l.append(i)
#     print(l)

# l={}

# for i in range(1,11):
#     name=input("Enter your name :")
#     l.update({i:name})
#     print(l)
# l=[1,2,2,5,2,1,4,2,1,2,5,3,6]

# s=set(l)
# print(list(s))

# import os
# os.mkdir("tables")

# def table(i):
#     tbl=""
#     for j in range(1,11):
#         tbl+= f"{i} x {j} = {i*j}\n"
#         with open(f"tables/table {i}.txt","w") as f:
#             f.write(tbl)

# for i in range(2,20):
#     table(i)

# sum=lambda a,b:print(a+b)
# sum(10,20)

# a=5
# b=10
# print("A")if a>b else print("=") if a==b else print("B")

# list=[1,2,5,3,4,7,8,56]
# if 2 in list:
#         print(list)
# else:
#         print("nothing in list")    

# list=["Tanvi","Ishu","Kriti"]
# name=input("Enter the name :")

#     if (name in list):
#         print(name)
#     else:
#         print("nommatch")    

# class parent:
#     name="Abhinav" 
#     salary="15k"

# a=parent()
# a.name="Garima"
# print(a.name,a.salary)   

# class parent:
#     def sum(self):
#         self.name="Abhinav"
#         self.salary="15k"
#         print(self.name,self.salary)

# a=parent()
# print(a.sum())

# class parent:
#     def info(self,name,salary):
#         self.name=name
#         self.salary=salary
#         print(f"My name is {self.name} and my salary is {self.salary}")
#     @staticmethod
#     def info2():
#         print("Done")

# a=parent()
# a.info("Garima","15k")     
# a.info2()   

# class parent:
#     a=1
#     def __init__(self):
#         print("Parent")

# class parent2:
#     c=3
#     def __init__(self):
#         print("parent2")        

# class child(parent,parent2):
#     b=2
#     def __init__(self):
#         super().__init__()
#         print("child")        

# a=child()        
# print(a.a,a.b,a.c)

# class parent:
#     a=1
#     print("Parent")

# class child(parent):
#     b=2
#     print("child")

# class child2(child):
#     c=3
#     print("child2")    

# a=child2()
    
# class info:
#     a="Abhinav"
#     @classmethod
#     def n(self):
#         print(f"My name is {self.a}")

# a=info()  
# a.a="Garima"
# a.name="Kriti"
# print(a.name)
# a.n()  

# def fun2(x):
#     def fx():
#         print("Good morning")
#         x()
#         print("Good night")
#     return fx        

# @fun2
# def fun():
#     print("Hello world")

# fun()

# class parent:
#     @property
#     def info(self):
#         self.name="Abhinav"
#         print(f"My name is {self.name}")
#     @info.setter   
#     def info2(self,salary):
#         self.salary=salary  
        
#         print(f"My salary is {self.salary} and id is {self.id}")  

# a=parent()
# a.info
# a.info2="20k"

# import random
# n=random.randint(1,100)
# a=-1
# guess=0

# while(a!=n):
#     a=int(input("Enter the number :"))
#     guess+=1
#     if(a>n):
#         print("'Lower number please")
#     else:
#         print("Hight number please")

# print(f"you attampt {guess}")

# computer=1
# list={
#     "s":1,
#     "p":0,
#     "c":-1
# }
# list2={
#     1:"Stone",
#     0:"Paper",
#     -1:"Syzer"
# }
# youstr=input("Enter your choice :")
# you=list[youstr]

# print(f"You choose {list2[you]} and computer choose {list2[computer]}")

# if(computer==you):
#     print("Draw try again")
# else:
#     if(computer==1 and you==0):
#         print("You win")
#     elif(computer==1 and you==-1):
#         print("You lose")
#     elif(computer==0 and you==1):
#         print("you lose")
#     elif(computer==0 and you==-1):
#         print("You Win")
#     elif(computer==-1 and you==0):
#         print("You lose")
#     elif(computer==-1 and you==1):
#         print("You Win")
#     else:
#         print("Something went wrong")                            


# computer=1
# list={
#     "s":1,
#     "p":0,
#     "c":-1
# }

# list2={
#     1:"Stone",
#     0:"Paper",
#     -1:"Cyzer"
# }

# a=input("Choose your char :")
# newlist=list[a]
# print(f"you choose {list2[newlist]} and computer choose {list2[computer]}")

# if(newlist==computer):
#     print("Match draw")
# else:
#     if(computer==1 and newlist==0):
#         print("You win")
#     elif(computer==1 and newlist==-1):
#         print("You lose")
#     elif(computer==-1 and newlist==0):
#         print("you loose")
#     elif(computer==-1 and newlist==1):      
#         print("You win")   
#     elif(computer==0 and newlist==-1):
#         print("ýou win")   
#     elif(computer==0 and newlist==1):
#         print("You loose")  
#     else:
#         print("Something went wrong")  

# import random

# n=random.randint(1,100)
# a=-1
# guess=0

# while(a!=n):
#     a=int(input("Enter the number :"))
#     guess+=1
#     if(a>n):
#         print("Enter lower number")
#     elif(a<n):
#         print("Enter hightest number")

# print(f"number is {n} attempt {guess}")

# for i in range(1,11):
#     print("*"*(11-i),end="")
#     print("")

# for i in range(1,5):
#     for j in range(i):
#         print("*",end=" ")
#     print("")    

# list =[]
# a=int(input("Enter number :"))

# for i in a:
#     list.append(i)
#     print(list)

# l={}

# for i in range(1,10):   
#     name=input("Enter your name :")
#     l.update({i:name})
#     print(l)

# l=[]

# for i in range(1,5):
#     name=input("Enter the name :")
#     l.append(name)
#     print(l)

# if(n:=len([1,2,1,5,2]))>3:                walrus operater
#     print(f"the length of {n} is greater then 3")

# if(n:=len([1,2,5,2,1,2,3,2]))>5:
#     print(n)

# a : int=4
# a:str="Abhinav"
# def fun(a:str,b:str):

# import typing

# a:typing.List[int]=[1,"a"]
# print(a)

# num=int(input("Enter the number :"))

# match num:
#     case 4:
#         print("num is 4")
#     case 10:
#         print("num is 5")
#     case 11:
#         print("num is 11")
#     case _:
#         print("inavlid")            

# a={
#     "a":"1",
#     "b":"2"
# }

# b={
#     "a":"2",
#     "c":"5"
# }

# marge=a | b
# print(marge)

# import name

# name.fun()

# if __name__=="__main__":

# list=[1,2,3,4,5,6,7,8,9,10]


# for index,i in enumerate(list,start=1):
#     if(index==4):
#         continue
#     else:
#         print(i)

# lists=[1,2,3,4,5,6,7]
# sum=lambda x:x+x

# add=map(sum,lists)
# print(list(add))

# lst=[1,2,3,4,5,6,7,8]
# sum=lambda x:x+x

# add=map(sum,lst)
# print(list(add))

# lists=[5,212,20,42,50,45,62,80,4]

# def sum(x):
#     if(x%5==0):
#         return True
#     return False

# div=filter(sum,lists)
# print(list(div))

# from functools import reduce

# lst=[1,2,3,4,5,6]

# def sum(a,b):
#     return a+b

# add=reduce(sum,lst)
# print(add)



# print(list.count(1))
# a=list.sort()
# print(a)
# tb=(1,2,3,4,5)

# v=list(tb)
# print(v)
# a=list(tb)
# print(a)

# list=[1,2,1,2,5]

# a=list.copy()
# a.reverse()
# print(a)

# tb=(1,2,3,4,5,6)

# print(dict(tb))

# a=[1,2,3,4,5,6,7,8,9]
# print(a[-5:-1])

# lst={1,2,1,2,12,5,2,12}
# lst1={1,2,5,4,8,6,2}

# lst3=lst.union(lst1)
# print(lst3)

# s=[1,1,1,2,2,3,3,5,5]
# a=set(s)
# b=list(a)

# obj={
#     "name":"Abhinav",
#     "salary":"78900"
# }

# del obj["name"]
# obj["city"]="Rohtak"

# print(obj["city"])

# print(obj.update({"name":"Garima"}))
# print(obj.get("name"))
# print(obj["name"],obj["salary"])

# def greet(xy):
#     def mx():
#         print("Good morning")
#         xy()
#         print("Good night")
#     return mx    
# @greet
# def hello():
#     print("Hello world")

# hello()    
# class parent:
#     def __init__(self,name):
#         self.name=name

# class child(parent):
#     def info(self):
#         print(self.name)        

# a=child("garima")
# print(a.info())

# class parent:
#     @property
#     def hlo(self):
#         print("Hello World")

# a=parent() 
# a.hlo    

# def sum(n):
#     if(n==1):
#         return 1
#     else:
#         return n + sum(n-1)

# print(sum(5))

# name=input("Enter the name :")

# if(name.startswith("www.")):
#     print("This is URL")
# elif(name.endswith("@gmail.com")):
#     print("Email id")
# else:
#     print(name)        

# a="hey my name \"is\" abhinav"
# print(a.replace("abhinav","Garima"))
# lst=[1,2,3,2,1,5,2,55,22,44,5,233]
# lst.pop(2)
# print(lst)



# lst=[1,2,1,1,2,1]
# a=set(lst)
# print(a)
# b=list(a)
# print(b)

# if(n:=len([1,2,3,4,5,6]))>5:
#     print(n)
# else:
#     print("dfd")    
# i=0

# while(i<=100):
#     print(i)
#     i +=1

# f=open("name.txt","w")
# f.write("Abhinav")
# f.close()

# f=open("name.txt","r")
# text=f.read()
# print(text)
# f.close()

# import os

# # os.mkdir("Python Tutorial")

# for i in range(1,101):
#     os.mkdir(f"Python Tutorial/Tutorial {i}")

# def table(i):
#     tbl=""
#     for j in range(1,11):
#         tbl+= f"{i} x {j} = {i*j}\n"
#         with open(f"tables/table {i}.txt","w") as f:
#             f.write(tbl)

# for i in range(2,20):
#     table(i)

# def tbl(i):
#     table=""
#     for j in range(1,11):
#         table+=f"{i} x {j} = {i*j}\n"
#         with open(f"Python Tutorial/Tutorial {i}/table {i}.txt","w") as f:
#                 f.write(table)



# for i in range(1,101):
#     tbl(i)

# name=["Abhinav","Garima","Tanvi","Kriti","Sweata","Ishu"]
# name1="::".join(name)
# print(name1)

# a=[]
# num=int(input("Enter the number :"))
# i=0
# while(i<num):
#     name=input("Enter your name : ")
#     a.append(name)
#     print(a)
#     i +=1

# a=[]
# num=int(input("Enter the number :"))

# for i in range(num+1):
#     name=input("Enter the name :")
#     a.append(name)
#     print(a)

# a={}
# num=int(input("enter the number :"))
# i=0
# while(i<num):
#     name=input("Enter the key :")
#     name2=input("Enter the value :")
#     a.update({name:name2})
#     print(a)

# a=[]
# i=0
# num=int(input("Enter the number :")) 
# while(i<=num):
#     name=input("Enter the name :")
#     a.append(name)
#     print(a)
#     i +=1

# a=[]
# num=int(input("Enter the number :"))

# for i in range(num+1):
#     name=input("Enter the name :")
#     a.append(name)
#     print(a)

# a={}
# num=int(input("Enter the number :"))
# i=0
# while(i<num):
#     name=input("Enter the key :")
#     name1=input("Enter the value :")
#     a.update({name:name1})
#     i +=1
#     print(a)

# a=[1,2,1,2,3,4,5,6]
# num=int(input("Enter the num :"))

# for i in range(len(a)+1):
#     name=int(input("Enter the key :"))
    
#     print(a)

# a=[1,2,1,2,3,4,5,6]

# num=int(input("Enter the num :"))
# print(a.count(num))

# a="Hey my name is Abhinav"

# for i in a:
#     print(i)

# for i in range(1,6):
#     print("*"*(6-i),end="")
#     print("")

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print("")    

# a=[]

# num=int(input("Enter the number :"))
# i=0
# while(i<num):
#     name=input("Enter the name :")
#     a.append(name)
#     i +=1
#     print(a)

# a=[]

# num=int(input("Ënter the number :"))

# for i in range(num+1):
#     name=input("enter name :")
#     a.append(name)
#     print(a)

# a={}
# i=0
# num=int(input("Enter the number :"))

# while(i<num):
#     name=input("Enter the key :")
#     name1=input("Enter the value :")
#     a.update({name:name1})
#     print(a)
#     i+=1

# sum=lambda x,y:x+y
# print(sum(10,20))

# x=int(input("Enter the number :"))
# y=int(input("Enter the number :"))

# print("X is greater")if x>y else print("x=y")if x==y else print("Y is greatest")

# list=[1,2,3,4,5,6,7,8,9]

# for index,i in enumerate(list):
#     if(index==3):
#         print(i)
#     else:
#         print("invaild")    

# def common():
#     name=input("Ënter first value :")
#     name1=input("Ënter second value :")
#     set1=set(name)
#     set2=set(name1)
#     lst=set1 & set2
#     print(lst)

# common()    

# year=int(input("Enter the year :"))

# if (year%400 == 0)and (year%100==0):
#     print("This is a leap year")
# elif (year%4 ==0) and (year%100 != 0):
#     print("this is a leap year")
# else:
#     print("Not a leap year")        

# a=int(input("Enter the value of a :"))
# b=int(input("Enter the value of b :"))
# c=int(input("Enter the value of c :"))

# if(a>b and a>c):
#     print("A is Greatest")
# elif(b>a and b>c):
#     print("B is Greatest")
# else:
#     print("C is greatest")        

# num=int(input("Enter the number :"))

# if(num==1):
#     print("Prime number")
# elif(num%2==0):
#     print("Not a prime number :") 
# else:
#     print("Prime number")     

# import random

# num=random.randint(1,100)
# guess=0
# a=-1

# while(a!=num):
#     a=int(input("Guess the number :"))
#     guess +=1
#     if(a>num):
#         print("Enter lower number")
#     elif(a<num):
#         print("Enter higher number")
#     elif(a==num):
#         print(f"You win the {a} is == {num} guess {guess}")        1*1*2*3*4

# num=int(input("Enter the number :"))
# fact=1
# if(num<0):
#     print("Enter vaild number :")
# elif(num==0):
#     print("Factroial of 0 is",1)
# elif(num>0):
#     for i in range(1,num+1):
#         fact*=i
# print(fact,"is a factrial number")       

# num=int(input("Enter the number :"))

# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# for i in range(1,6):
#     print("*"*i,end="")
#     print("")

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print("")    

# import os

# os.mkdir("Tables")

# import os

# # for i in range(2,101):
# #     os.mkdir(f"Tables/Table {i}")

# def table(a):
#     tbl=""
#     for i in range(1,11):
#         tbl+=f"{a} x {i} = {a*i}\n"
#         with open(f"Tables/Table {a}/table{a}.txt","w") as f:
#             f.write(tbl)


# for i in range(2,101):
#     table(i)

# a=[]
# num=int(input("Enter the number :"))
# i=0
# while(i<num):
#     name=input("Enter your name :")
#     a.append(name)
#     i+=1
#     print(a)

# a=[]
# num=int(input("Enter the number :"))

# for i in range(1,num+1):
#     name=input("Enter the name :")
#     a.append(name)
#     print(a)

# a={}

# num=int(input("Enter the number :"))
# i=0

# while(i<num):
#     name=input("ENter the key :")
#     name1=input("Entr the value :")
#     a.update({name:name1})
#     print(a)
#     i+=1

# a=[1,2,5,8,5,6,7,9,6,4]

# print(a.count(5))
# a=[1,2,1,2,0]

# b=a.copy()
# b.reverse()
# print(b)

# if(n:=len([1,2,5,4,5,4,5]))>5:
#     print(n,"is greatest")
# else:
#     print("n is lower")    

# num1=int(input("Enter the number :"))
# num2=int(input("Enter the second number :"))
# choose=input("Choose one +,-,*,%,** :")
 
# if(choose=="+"):
#     print(f"{num1} + {num2} = {num1+num2}") 
# elif(choose=="-"):
#     print(f"{num1} - {num2} = {num1-num2}")    
# elif(choose=="*"):
#     print(f"{num1} * {num2} = {num1*num2}")
# elif(choose=="%"):
#     print(f"{num1} % {num2} = {num1%num2}")
# elif(choose=="-"):
#     print(f"{num1} ** {num2} = {num1**num2}") 
# else:
#     print("Choose vaild syntax")    

# a=["Abhinav","Garima"]

# if("Abhinav" in a):
#     print("True")

# a=["Garima","Tanvi","Kriti","Ishu","Sweata"]

# name=input("Enter the name :")

# if(name in a):
#     print(f"Abhinav i think {name} is your ex")
# else:
#     print("unknown")

# a="Hey my name is Abhinav"
# w=a.split(" ")

# for i in range(len(w)):
#     w[i]=w[i].lower()

# w.sort()
# print(w)   

# a={
#     "name":"Abhinav",
#     "city":"Rohtak"
# }
# b={
#     "Address":"Rohtak",
#     "name":"Garima"
# }

# c=a|b
# print(c)

# obj={
#     "name":"Abhinav"
#     obj={
#        "name":7 
#     }
# }

# a=["as"]

# if not a:
#     print("List is empty")
# else:
#     print("List is not empty")  

# a=[1]

# if(len(a)==0):
#     print("List is empty")
# else:
#         print("List is not empty")

# try:
#     number =int(input("Enter the number :"))
#     number1 =int(input("Enter the number :"))
#     if number>number1:
#         print("number is greatest")
#     else:
#         print("number1 is greatest")
# except ValueError as v:
#     print(v,"dfdsdskmk")        

# a=[1,2,5,2,3,5]
# b=[5,2,5,6,77,1,22]
# c=a|b
# print(c)

# name1="Kriti"
# name2="Tanvi"
# set1=set(name1)
# set2=set(name2)
# lst=set1 & set2
# print(lst)

# year=int(input("Enter the year :"))

# if(year%400==0)and(year%100==0):
#     print(f"{year} is a leap year")
# elif(year%4==0)and(year%100!=0):
#     print(f"{year} is a leap year")
# else:
#     print("Not a leap year")        

# l=["s"]

# if(not l):
#     print("List is empty")
# else:
#     print("List is nit empty")    

# l=[]

# if(len(l)==0):
#     print("list is empty")
# else:
#     print("Not empty")    
# import random 

# computer=random.randint(0,2)

# list={
#     "s":1,
#     "p":0,
#     "c":2
# }
# list1={
#     1:"Stone",
#     0:"Paper",
#     2:"Cyzer"
# }

# print("Choose s for Stone\nChoose p for paper\nChoose c for Cyzer")
# a=input("enter the value :")
# newlist=list[a]
# b=list1[newlist]
# c=list1[computer]

# print(f"you choose {b} and computer choose {c}")


# if(computer==newlist):
#     print("Match draw try again")
# else:
#     if(computer==1 and newlist==0):
#             print("You win")
#     elif(computer==1 and newlist==2):
#             print("You loose")
#     elif(computer==0 and newlist==1):
#             print("you loose")        
#     elif(computer==0 and newlist==2):
#             print("You win")
#     elif(computer==2 and newlist==0):
#             print("You loose")
#     elif(computer==2 and newlist==1):
#             print("You win")
#     else:
#             print("Invaild number")  
# try:
#     num1=int(input("Enter first number :"))                
#     num2=int(input("Enter second number :")) 
#     print("Choose + for Addtion\nChoose - for Substration\nChoose * for Multiplication")
#     choose=input("Enter the operater :")
#     if(choose=="+"):
#         print(f"{num1} + {num2} = {num1+num2}")
#     elif(choose=="-"):
#         print(f"'{num1} - {num2} = {num1-num2}")
#     elif(choose=="*"):
#         print(f"'{num1} * {num2} = {num1*num2}")
#     else:
#         print("Invaild number")  
# except ValueError as v:
#             print(v)

# num=int(input("Enter the number :"))
# i=1

# while(i<=num):
#     print("*"*i,end="")
#     print("")
#     i+=1

# num=int(input("Enter the number :"))

# for i in range(1,num+1):
#     print("*"*((num+1)-i),end="")
#     print("")

# for i in range(1,6):
#     for j in range(i):
#         print("*"*(6-j),end=" ")
#     print("")    

# a=[]
# num=int(input("Enter the number :"))
# i=0

# while(i<num):
#     name=input("Enter the value :")
#     a.append(name)
#     i+=1
#     print(a)

# a=[]
# num=int(input("Enter the num :"))

# for i in range(1,num+1):
#     name=input("Enter the value")
#     a.append(name)
#     print(a)
    
# a={}
# num=int(input("Enter the number :"))
# i=0
# while(i<num):
#     name1=input("Enter the key :")
#     name2=input("Enter the value :")  
#     a.update({name1:name2})
#     print(a)
#     i+=1  

# a={}
# num=int(input("Enter the number :"))

# for i in range(1,num+1):
#     name1=input("Enter the key :")
#     name2=input("Enter the value :") 
#     a.update({name1:name2})
#     print(a)
# import os

# os.mkdir("Tables")

# import os

# for i in range(2,101):
#     os.mkdir(f"Tables/Table {i}")


# def table(n):
#     tbl=""
#     for i in range(1,11):
#         tbl += f"{n} x {i} = {n*i}\n"
#         with open(f"Tables/Table {n}/Table {n}.txt","w") as f:
#             f.write(tbl)


# for i in range(2,101):
#     table(i)

# a={
#     "name":"Abhinav"
# }
# b={
#     "city":"Rohtak"
# }

# c=a|b
# print(c)

# a=(1,2,3,4)
# b=(5,6,1,2,3)
# c=a + b
# print(c)

# for index,i in enumerate(range(101)):
#     if(index==51):
#         break
#     else:
#         print(i)

# a=5
# b=10
# print("A") if (a>b) else print("=") if(a==b) else print("B")

# sum=lambda x,y:print(x+y)
# sum(10,20)

# print((lambda x:x+x)(5))

# class parent:
#     name="Abhinav"
#     city="Rohtak"

# a=parent()
# a.name="Garima"
# a.rollno="1010"
# print(a.name,a.rollno)    

# class parent:
#     def info(self):
#         print("Hello")

# a=parent()
# a.info()        

# class parent:
#     def __init__(self,name):
#         self.name=name

#     def info(self):
#         print(self.name)    
        

# a=parent("Abhinav")
# a.info()     

# class parent:
#     def __init__(self):
#         self.a=[1,2,3,4,5,6,7,8,9]

# class child(parent):
#     def info(self):
#         print(self.a)    

# class child2(child):
#     def reverse(self):
#         self.a.reverse()
#         print(self.a)            

# a=child2()
# a.reverse()

# class parent1:
#     def __init__(self,name):
#         self.name=name

# class parent2:
#     def __init__(self,city):
#         self.city=city

# class child(parent1,parent2):
#     def info(self):
#         print(self.name)
#         # print(self.city)

# a=child("Abhinav")
# a.info()

# class parent:
#     def __init__(self):
#         print("Hello")

# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("World")        

# a=child()        

# if(n:=len([1,2,3,4,5,6,7,8,9]))<5:
#     print(n)
# else:
#     print("5 is smaller")

# def greet(xy):
#     def mz():
#         print("Good morning")
#         xy()
#         print("Good night")
#     return mz        

# @greet
# def hello():
#     print("Hello World")

# hello()    

# i=1
# num=int(input("Enter the number :"))

# while(i<=num):
#     print("*"*(6-i),end="")
#     print("")
#     i+=1

# num=int(input("Enter the number :"))

# for i in range(1,num+1):
#     for j in range(6-i):
#         print("*",end=" ")
#     print(" ")    

# a=[2,4,5,6,8,7,5,2]

# for i in a:
#     if i%2==0:
#         a.remove(i)
#     else:
#         print(i) 
# a=[2,4,5,6,8,7,5,2]
# a.insert(2,55)  
# print(a) 

# a=[]
# num=int(input("Enter the number :"))

# for i in range(1,num+1):
#     name=input("Enter the name :")
#     a.append(name)
#     print(a)

# a=[]
# i=1
# num=int(input("Enter the number :"))

# while(i<=num):
#     name=input("Enter the name :")
#     a.append(name)
#     i+=1
#     print(a)

# import os

# # os.mkdir("Tables")

# def table(n):
#     tbl=""
#     for i in range(1,11):
#         tbl+=f"{n} x {i} = {n*i}\n"
#         with open(f"Tables/Table {n}/Table {n}.txt","w") as f:
#             f.write(tbl)

# for i in range(2,101):
#     table(i)

# a=[]
# i=1
# num=int(input("Énter the value :"))

# while(i<=num):
#     name=input("Enter the value :")
#     a.append(name)
#     i+=1
#     print(a)

# str1=input("énter the name :")
# str2=input("enter the name: ")
# s1=set(str1)
# s2=set(str2)
# lst=s1 & s2
# print(lst)

# a={}
# num=int(input("Enter the number :"))

# for i in range(1,num+1):
#     name=input("Enter the name :")
#     name2=input("Enter the name :")
#     a.update({name:name2})
#     print(a)

# lst:list[str,int]=["Abhinav",2]
# print(lst)

# if (n:=len([1,2,3,4]))<5:
#     print("N is less than 5")

# a=int("5")
# b=5.5
# sum=a+b
# print(sum)
# print(type(True))

# a="Hey my name is abhinav"


# print(a.count("a"))
# a=[1,2,1,2,3,5,4,2,3,]

# for i in range(1):
#     index=int(input("Enter index number :"))
#     add=input("Enter the value you want to add:")
#     a.insert(index,add)
#     print(a)

# a=[]
# num=int(input("Enter the number how many time you add content on list :"))
# i=1

# while(i<=num):
#     name=input("Enter the value :")
#     a.append(name)
#     a.sort()
#     print(a)
#     i+=1

# a=[2,1,2,5,22]

# for i in range(1):
#     dlt=int(input("enter the number you want to delete :"))
#     a.remove(dlt)
#     print(a)

# def sum(*args):
#     for i in args:
#         print(i+i)

# sum(1,2,3,4,5)    

# def sum(a):
#     if(a==0 or a==1):
#         return 1
#     else:
#         return a +sum(a-1)
    
# print(sum(5))    

# i=0

# def sample():
#     print("im sample function")
#     if(i<5):
#         sample()
#         print("Back to sample function")

# sample()           




# a="My name is Abhinav"

# for i in range(1):
#     find=input("Choose the word for replace :")
#     rpl=input("Enter new word :")
#     b= a.replace(find,rpl)
#     print(b)




# for i in range(0,1):
#     value=input("Enter value for count :")
#     print(a.count(value))

# print(a.endswith("abhinavs"))

# print(a[1:5])

# i=0

# while(i<=len(a)-1):
#     print(a[i])
#i     i+=1
# import random 

# obj={
#     "s":1,
#     "c":0,
#     "p":2
# }
# obj2={
#     1:"Stone",
#     0:"Cyzer",
#     2:"Paper"
# }
# computer=random.randint(0,2)
# print("Choose s for Stone\nChoose c for Cyzer\nChoose P for Paper")
# choose=input("Enter the value you choose :")
# lst=obj[choose]
# lst2=obj2[lst]
# lst3=obj2[computer]
# print(f"You choose {lst2} and computer choose {lst3}")


# if(computer==lst):
#     print("Match Draw")
# else:
#     if(computer==1 and lst==2):
#         print("You Win")
#     elif(computer==1 and lst==0):
#         print("You loose")
#     elif(computer==2 and lst==1):
#         print("You loose")
#     elif(computer==2 and lst==0):
#         print("You Win")
#     elif(computer==0 and lst==1):
#         print("You Win")
#     elif(computer==0 and lst==2):
#         print("You loose")    
#     else:
#         print("Choose valid value")                    

# class parent:
#     name="Abhinav"

# a=parent()
# a.name="Garima"
# print(a.name)    

# class parent:
#     a=5
#     def sum(self,a,b):
#         self.a =a
#         self.b =b
#         print(a + b)

# a=parent()
# a.sum(10,20)

# class parent:
#     a=5 
#     @staticmethod
#     def hlo():
#         print("Hello World")

# a=parent()
# a.hlo()        

# class parent:
#     def info(self):
#         self.name="Abhinav"
#         print("Hi")

# a=parent()
# a.info()   
# a.name    

# class parent:
#     name="Abhinav"
#     @classmethod
#     def info(self):
#         print(f"My name is {self.name}")

# a=parent()
# a.name="Garima"
# a.info()      
# b=parent()
# b.info()  

# import random

# num=random.randint(1,100)

# guess=0
# a=-1

# while(a!=num):
#     a=int(input("Guess the number :"))
#     guess+=1
#     if(a>num):
#         print("Çhoose Lower value :")
#     elif(a<num):
#         print("Çhoose higher value")
#     elif(a==num):
#         print(f"You win {a} is == {num} guess {guess}")
    
# def status(x):
#     match x:
#         case 200:
#             print("Status Ok")
#         case 404:
#             print("Data not found")
#         case 500:
#             print("Server Error")
#         case _:
#             print("Unknown Status")            

# status(4045)            

# with (
#     open("name.txt","+w") as f,
#     open("name2.txt","+w") as x
# ):
#     f.write("Hello")
#     x.write("Hello World")

# num=int(input("Énter the number :"))

# if(num==str):
#     raise ValueError("You enter only integer number :")
# else:
#     print(num)

# try:
#     a=int(input("Enter first number :"))
#     b=int(input("Enter first number :"))
#     if(a>b):
#         print(f"{a} is Greatest")
#     elif(a<b):
#         print(f"{b} is greatest")
#     else:
#         print(f"{a} == {b}")
# except Exception as e:
#     print(e)  
# else:
#     print("Done")    

# import python1

# python1.hello()

# lst=[1,2,3,45,6,4,5,85,6,2]

# for index,i in enumerate(lst):
#     if(index==5):
#         break
#     else:
#         print(i)    

# lst=["Garima","Abhinav","Tanvi","Kriti"]

# result="||".join(lst)
# print(result)
# print(lst)

# str1="My name is {} and i'm from {}".format("Abhinav","Rohtak")
# print(str1)

# def sum(a):
#     return a+1
# lst=[1,2,3,4,5]
# lists=map(sum,lst)
# print(list(lists))

# def sum(a,b):
#     return a+b
# lst=[1,2,3,4,5]

# lists=filter(sum,lst)
# print(list(lists))

# lists=[5,212,20,42,50,45,62,80,4]

# def sum(x):
#     if(x%5==0):
#         return True
#     return False

# div=filter(sum,lists)
# print(list(div))

# a=[]
# num=int(input("Enter the number :"))
# i=0

# while(i<num):
#     name=input("Enter the value :")
#     a.append(name)
#     a.sort()
#     i+=1
#     print(a)

# a=[]
# num=int(input("Enter the number :"))

# for i in range(1,num+1):
#     name=input("Enter the value :")
#     a.append(name)
#     a.sort()
#     print(a)

# a={}
# num=int(input("Enter the number :"))
# i=1

# while(i<=num):
#     name=input("Enter the value :")
#     name2=input("Enter the key :")
#     a.update({name:name2})
#     print(a)
#     i+=1

# str=input("Enter the string :")
# print(str)

# for i in range(1):
#     find=input("Enter the value :")
#     str1=str.count(find)
#     print(str1)

# lst=[1,2,36,5,4,8,56,9]

# for i in range(1):
#     index=int(input("Enter the index no you want to replace :"))
#     add=int(input("Enter the value :"))
#     lst.insert(index,add)
#     print(lst)

# lst=[1,2,3,4,5,6,7,8,9]

# for i in range(1):
#     num=int(input("Enter the number :"))
#     lst.pop(num)
#     print(lst)

# str=input("Enter the string :")
# print(str)

# for i in range(1):
#     rem=input("Enter the remove value :")
#     add=input("Enter the add value :")
#     str1=str.replace(rem,add)
#     print(str1)

# lst=[1,2,3,4,5,6,7,8,9]

# lst.reverse()
# print(lst) 

# import os

# def table(a):
#     tbl=""
#     for i in range(1,11):
#         tbl+=f"{a} x {i} = {a*i}\n"
#         with open(f"Tables/Table {a}/table {a}.txt","w") as f:
#             f.write(tbl)

# for i in range(2,101):
#     table(i)

# a=[]
# num=int(input("Enter the number :"))
# i=1

# while(i<=num):
#     name=input("Enter your name :")
#     a.append(name)
#     a.sort()
#     print(a)
#     i+=1

# a={}
# num=int(input("Entr the number :"))

# for i in range(1,num+1):
#     name=input("Enter the value :")
#     name2=input("Enter the key :")
#     a.update({name:name2})
#     print(a)

# i=1

# while(i<=5):
#     print("*"*i,end="")
#     print("")
#     i+=1

# for i in range(1,6):
#     print("*"*(6-i),end="")
#     print("")

# for i in range(1,6):
#     for j in range(6-i):
#         print("*",end=" ")
#     print("")    

# lst=[1,2,3,4,5,6,5,1,2,35,4,4,4]

# for i in range(1):
#     idx=int(input("Enter the index no :"))
#     name=int(input("Enter the number :"))
#     lst.insert(idx,name)
#     print(lst)


# for i in range(1):
#     find=int(input("Enter the find value :"))
#     print(lst.count(find))
# year=int(input("Enter the year :")) 

# if(year%400==0 and year%100==0):
#     print("Leap year")
# elif(year%4==0 and year%100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")    
# def greet(xy):
#     def mz():
#         print("Good morning")
#         xy()
#         print("Good night")
#     return mz    

# @greet
# def hello():
#     print("Hello world")

# hello()   

# sum=lambda x,y:print(x+y)
# sum(10,220) 

# print((lambda x,y:x+y)(50,10))
# num1=int(input("Enter the num1 :"))
# num2=int(input("Enter the num2 :"))

# print("A") if(num1>num2) else print("=") if(num1==num2) else print("B")

# def sum():
#     """This is use for sum two numbers"""
#     return 10+20

# print(sum())
# print(sum.__doc__)

# a="Hey my name is {}".format("Abhinav")
# print(a)

# def cube(i):
#     return i*i*i

# lst=[1,2,3,4,5]
# newlst=[]
# for i in lst:
#     newlst.append(cube(i))
#     print(newlst)

# print(newlst) 

# lst=[1,2,3,4,5] 
# def sum(i):
#     return i*i*i

# newlst=map(sum,lst)
# print(list(newlst))  

# def cube(i):
#     return i*i*i

# lst=[1,2,3,4,5]

# newlst=map(cube,lst)
# print(list(newlst))
# newlst=[]

# for i in lst:
#     newlst.append(cube(i))

# print(newlst) 

# def cube(i):
#     return i*i*i
# lst=[1,2,3,4,5]

# newlst=[]
# for i in lst:
#     newlst.append(cube(i))

# print(newlst)    
# def filters(i):
#     return i%2==0

# lst=[1,2,3,4,5,6]

# newlst=filter(filters,lst)
# print(list(newlst))
# newlst=[]
# for i in lst:
#     newlst.append(filters(i))

# print(newlst)
# newlst=filter(filters,lst)
# print(list(newlst))
# def fl(i):
#     return i%2==0

# lst=[2,3,4,5,6,8,16,15,16]

# newlst=filter(fl,lst)
# print(list(newlst))

# def cube(i):
#     return i*i*i

# lst=[1,2,3,4,5]

# newlst=map(cube,lst)
# print(list(newlst))

# lst=[1,2,3,4,5]
# newlst=map(lambda x:x*x*x,lst)
# print(list(newlst))

# lst=[1,2,3,4,5]
# newlst=filter(lambda x:x%2==0,lst)
# print(list(newlst))

# lst=[1,2,3,4,5]
# newlst=filter(lambda x:x>2,lst)
# print(list(newlst))
# def cube(i):
#     return i*i*i 

# lst=[1,2,3,4,5]
# newlst=[]
# for i in lst:
#     newlst.append(cube(i))
    
# print(list(newlst))    
    
# lst=[1,2,3,4,5]

# newlst=map(lambda x:x*x*x,lst)
# print(list(newlst))

# if(n:=len([1,2,3,4,5,6,7,8,9]))>5:
#     print("Win")

# lst:list[str,int]=[1,"5"]
# print(lst)

# a={
#     "name":"harry",
#     "from":"india",
#     "marks":[92,98,96]}

# a["name"]="Abhinav"
# print(a["name"])
# print(a["marks"][0])
# import random

# lst={
#     "s":1,
#     "p":2,
#     "c":0
# }
# lst2={
#     1:"Stone",
#     2:"Paper",
#     0:"Cyzer"
# }
# computer=random.randint(1,2)
# print(f"Choose S from Stone\nChoose P for Paper\nChoose C for Cyzer")
# choose=(input("Choose one :"))
# a=-1
# newlst=lst[choose]

# print(f"You choose {lst2[newlst]} and computer choose {lst2[computer]}")


# if(computer==newlst):
#     print("Draw")
# else:
#     if(computer==0 and newlst==1):
#         print("You win")
#     elif(computer==0 and newlst==2):
#         print("You loose")
#     elif(computer==1 and newlst==0):
#         print("You loose")  
#     elif(computer==1 and newlst==2):
#         print("You win")
#     elif(computer==2 and newlst==0):
#         print("You win")
#     elif(computer==2 and newlst==1):
#         print("You loose") 
#     else:
#         print("Invaild number")                          

# computer=1
# list={
#     "s":1,
#     "p":0,
#     "c":-1
# }
# list2={
#     1:"Stone",
#     0:"Paper",
#     -1:"Syzer"
# }
# youstr=input("Enter your choice :")
# you=list[youstr]

# print(f"You choose {list2[you]} and computer choose {list2[computer]}")

# if(computer==you):
#     print("Draw try again")
# else:
#     if(computer==1 and you==0):
#         print("You win")
#     elif(computer==1 and you==-1):
#         print("You lose")
#     elif(computer==0 and you==1):
#         print("you lose")
#     elif(computer==0 and you==-1):
#         print("You Win")
#     elif(computer==-1 and you==0):
#         print("You lose")
#     elif(computer==-1 and you==1):
#         print("You Win")
#     else:
#         print("Something went wrong")                            

# class parent:
#     def __init__(self):
#         print("Parent")

# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("Child")   

# a=child()
