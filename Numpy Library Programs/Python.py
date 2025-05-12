# Day 2
"""
Built-in Function
print, input, int, float
#input :-> return string/text value
"""

#Write a program to calculate gross salary of an employee where HRA is 20% and DA is 30% of his basic salary.
#Hint :- Gross salary = BasicSalary + HRA + DA
'''
bs = float(input("Enter the basic salary:"))
hra = bs*20/100
da = bs*30/100
gs = bs+hra+da
print("Gross salary", gs)
'''

'''
Python operators:-
Arithmetic Operators (Binary Operator)
+,-,*,/,%,//,** a+b (a,b operand, + operator)
a = 7
b = 5
a+b = 12
a-b = 2
a*b = 35
a/b = 1.4
a%b = 2 (modulus) (reminder)
a//b = 1 (truncation/floor division)
a**b = 16807 (Exponential(power))

Realtional Operators / Conditional operators (Binary Operator)
(Result Boolean True/False)
>,<,>=,<=,==,!=
a = 7
b = 5
a>b : True
a<b : False
a>=b : True
a<=b : False
a==b : False
a!=b : True

Membership Operators
(Boolen Value Result/ True/ False) (Check Existance)
in, not in
a = "aman"
b = "amankumar"

a in b :True
b in a :False
'm' in a :True
'mn' in a:False
'mn' not in a:True

Indentity operator
(Boolen Value Result/ True/ False) (Check Exact Match)
is, is not
a = 'aman'
b = 'amankumar'
c = 'aman'
a is b: False
a is c:True (work like a == c)
a is not b: True (work like a!=b)
a is not c: False

Assignment Operator
=,+=,-=,*=,/=,%= etc
a = 10
a += 1 : 11
a -= 1 : 9
a *= 1 : 10
a /= 1 : 0
a %= 1 : 1

# Day 3
Logical Operators
AND, OR, NOT
True and True
print(10<5 and 10>5) :- False
print(10<50 and 10>5) :- True

OR
print(10<5 and 10>5) :- True

NOT(unary operator)
print(not 10>5) :- False

Bitwaise Operator
~ Tiled operator/ Complementary Value (unary operator)
and &
or |
Right Shift Operator >>
Left Shiflt Operator <<
XOR gate :- ^

a = -6
print(~a) = 5
a = 5
print(~a) = -6

'''
# Day 4
"""
Literals
Number:- (int,float,complex)
    integer
    float
    binary (0b11)
    hexadecimal (0x123)
    octal (0o123)
    complex_Number
a = 10
print(a)
print(type(a)) (int)

a = 0b10001
print(a)
print(type(a)) (binary)

String:- (str)
   character
   string/text
a = "hello"
print(type(a)) (str)
"""

"""
Conditional Statement:-
if,if_else,elif,Nested if_else,Complex Condition
Loops:-
for, while

if syntax:-
if(condition):
     True_statement
else:
     False_Statement

Nested if_else:-
if(condition):
     if(condition):
         True_statement
     else:
         False
else:
     False_Statement

else:
     False_Statement

Complex Conditions:- Those programs which use logical operators with condition statement

"""
# WAP to find greater value among three
"""
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
if(a>b and a>c):
    print("A is the greater number")
elif(a<b and b>c):
    print("B is the greater number")
else:
    print("C is the greater number")
"""

#WAP to check an entered character is vowel or consonants:
"""
ch = input("Enter the character:")
if(ch in "AEIOUaeiou"):
    print("Vowel")
else:
    print("consonants")
"""
# Day 5
"""
Loops:-
for, while

syntax:
for

for variable_name in range(start,stop,step):
   statements
# bydefault: step = 1, start = 0
for a in range(5):
  print(a)

#break(it exist from the current loop), continue(it will continue to the loop), pass
for a in range(1,11):
    if(a==5):
        break
    print(a)

    
for a in range(1,11):
    if(a==5):
        continue
    print(a)

for a in range(1,11):
    if(10>5):
      pass
# loops agar pura chalega to else chalega agar loop nhi chalega pura toh else bhi nhi chalega
for a in range(5):
    print(a)
else:
    print(0)
"""
#Day 6

"""
While loop
initialization
while(condition):
    statements
    incr/decr

a = 1
while(a<=5):
    print("hello")
    a=a+1

"""
#Day 7
#Nested Loop(pattern building)
# Find All Prime Number from 1 to 100
'''
for num in range(1,101):
    count = 0
    for i in range(1,num+1):
        if(num%i==0):
            count=count+1
    if(count==2):
        print(num)
'''

"""
*****
*****
*****
*****
*****
print("*****\n*****\n*****\n*****\n*****")
"""
'''
for i in range(1,11): #rows
    for j in range(1,21):#columns
        print("*",end="")
    print()
'''
"""
*
**
***
****
*****
"""
'''
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
'''

"""
     *
    **
   ***
  ****
******
"""
'''
for i in range(1,6):
    for k in range(5,i,-1):
        print(end=" ")
    for j in range(1,i+1):
        print("x",end="")
    print()        
'''

"""
     *
    * *
   * * *
  * * * *
 * * * * *
"""
'''
for i in range(1,6):
    print(" "*(5-i)+"* "*i)
'''

"""
1
12
123
1234
12345
"""
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''

"""
1
22
333
4444
55555
"""
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
'''

"""
1
23
456
78910
11121314
"""
'''
c=1
for i in range(1,6):
    for j in range(1,i+1):
        print(c,end="")
        c=c+1
    print()
'''

"""
1
01
010
1010
10101
"""
'''
c=3
for i in range(1,6):
    for j in range(1,i+1):
        print(c%2,end="")
        c=c+1
    print()
'''
"""
0
10
101
0101
01010
"""
'''
c=2
for i in range(1,6):
    for j in range(1,i+1):
        print(c%2,end="")
        c=c+1
    print()
'''

"""
A
AB
ABC
ABCD
ABCDE
"""
'''
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()
'''
"""
0
909
89098
789087
678909876
56789098765
4567890987654
345678909876543
23456789098765432
1234567890987654321
"""
'''
s = '0'
for i in range(10,0,-1):
    if(i!=10):
      s = str(i)+s+str(i)
    print(s)
'''

#Day 8
"""
Sequence Data Type:- List, Tuple
a = 10
# Creating a list
a = [12,32,3,44,55,34,90]
a = []
a = [12,12.2,True,'A','aman'] list is heterogines datatype
a = list()
a = list([2,3,5,6,7])
a = [x for x in range(1,11,1)] using loops
print(a)

# Indexing forward 
a = [2,5,6,8,8,9]
print(a[2])

# Indexing backward
a = [2,5,6,8,8,9]
print(a[-4])

# Slicing
a = [2,3,4,6,7]
print(a[2:4:2])

a = [2,3,4,6,7]
print(a[-1:-4:-1])

# Replication
a = [2,3,4,5]
print(a*2)

# Traversing
a = [2,5,6,7,8,9]
for x in a:
   print(x)

# Update a list
a = [2,5,6,7,8]
a[3] = 99
print(a)

del a[3]
print(a)

# Functions (built-in) len, sum, min, max
a = [2,3,4,5]
print(len(a))
print(sum(a))
print(min(a))
print(max(a))

# Methods- append, insert, extend, copy, pop, remove, sort, reserve, count, clear, index
a = [2,3,4]
b = [5,6,7]
a.extend(b)
print(a)

a = [2,3,4]
b = a.copy()
print(b)

a = [2,3,4,3,3]
print(a.count(3)) (sum,max,min,len)

lists = [2,3,4,5,6,7,8,9]
for x in lists:
    print([x*m for m in range(1,11)])

"""

#Day 9
"""
Tuple:- Sequence Data Type

#The following ways to Creating the tuple
t = (2,3,4,5,6,7)
t = (23,234.45,True,"Aman",'A',3+9i) tuple is also a heterogenis datatype
t = ()
t = tuple()
t = tuple([3,4,5,6,8)]
print(t)

#Indexing forward
t = tuple([3,4,5,6,8)]
print(t[2])

#Indexing backward
t = tuple([3,4,5,6,8)]
print(t[-2])

#Slicing
t = tuple([3,4,5,6,8)]
print(t[0:3)]

t = tuple([3,4,5,6,8)]
print(-4:-1)

#Replication
t = tuple([3,4,5,6,8)]
print(t*3)

#Traversing
t = tuple([3,4,5,6,8)]
for x in t:
print(x)

#Delete tuple
t = tuple([3,4,5,6,8)]
del t[2]

#Functions(built-in) sum, min, max, len

#Methods: count, index
"""

#Day 10
"""
SET
s = {2,3,4,5,6,7,8}
set do not support duplicate values
set do not support
set do not support slicling
set do not support replication
set supoort traversing
s = {3,4,5,6,7}
for i in s:
    print(i)

#The way to create sets
s = {2,3,4,5,6,7,8}
s = {}
s = set([2,3,4,5,7)]
s = set()

#Dictionary
{key:value}//pair(items)
dic do not support duplicate keys
dic support duplicate values
dic do not support replication
"""

#Day 11
"""
STRING:- It is a collection of characters
It is immutable
s = 'Aman' (string is a collection of characters and it behave like tuple)
#replication
#indexing
#slicling
#transerve
for x in s:
   print(x)
print(s)

ASCII VALUES -> A - 65 - 1000001
                a - 97 - 1100001
"""

'''
a = 'B'
print(ord(a))

a = 'z'
print(ord(a))

a = 'A'
print(bin(ord(a)))

a = 65
print(chr(a))
'''

#Day 12
#Built-in Library
"""
import library_name
from library_name import method1,method2....
1.Math Library (factorial,ceil,floor,power,sqrt,sin,cos,tan,cot,sinh,cosh etc
log,log10,exponient,pi etc

2.Random Library
random, randint

3.DateTime Library

"""
'''
# Math Library
import math

print(math.factorial(7))
print(math.ceil(8.12)) #forward roundoff
print(math.floor(8.12)) #backward roundoff
print(math.pow(3,3))
print(math.sqrt(64))
print(math.pow(27,1/3)) #cube root
print(math.ceil(math.pow(64,1/3)))
print(math.pi)
print(math.sin(45*math.pi/180))
print(math.log(1))

from math import sqrt,factorial
print(sqrt(25))

# Random Library

import random
print(random.randint(1,6))

print(random.randint(1000,9999))

# DateTime Library

import datetime
print(datetime.datetime(2025,3,5))

time = datetime.datetime.now()
print(time.year)
print(time.month)
print(time.day)
'''

#Day 13
"""
Functional Programming

Functions in Python
def function_name(arugment):
     definition

function_name(parameter)
"""
'''
def greeting():
    print("Good Morning!")
greeting()

def add(x,y):
    return x+y
    
a = int(input("Enter A Number:"))
b = int(input("Enter B Number:"))
print(add(a,b))
'''
'''
def checkPrime(num):
    count = 0
    for i in range(1,num+1):
        if(num%i==0):
            count=count+1
    if(count==2):
        return "Prime"
    else:
        return "Not Prime"
print(checkPrime(18))
'''
'''
def checkPrime(num):
    count = 0
    for i in range(1,num+1):
        if(num%i==0):
            count=count+1
    if(count==2):
        return True
    else:
        return False

for a in range(1,101):
    if(checkPrime(a)):
        print(a,end="  ")
'''
'''
def addElement(li):
    return sum(li)

lis = [2,34,54,6,77,89,3]
print(addElement(lis))
'''

#Day 13
#File Handling
"""
Types of file
1-Text File
2-Binary File

Syntax:-
file_object = open('file_name.extension','mode')

Mode:-
r, w, a, r+, w+, a+
write, writeline
read, readline, readlines

file = open('student.txt','a')
file.write('Hello World')
file.close()

file = open('student.txt','r')
data = file.read()
print(data)

file = open('student.txt','r')
data = file.read(5)
print(data)

file = open('student.txt','r')
data = file.readline()
print(data)   
"""
#For binary files
#dump, load
"""
Binary File
file_object = open('file_name.extension','mode')
mode:- rb, wb, ab, rb+, wb+, ab+

import pickle
file = open('student.dat','wb')
pickle.dump('hello india',file)
file.close()

import pickle
file = open('student.dat','rb')
data = pickle.load(file)
print(data)
file.close()
"""

#Error/Exception Handling
"""
Types of Error:-
Syntax Error/ Compile Time Error / Error (fix)
Logical Error / Runtime Error / Exception (handling)
Semantic Error(logic Error)
try except finally

a = '10'
b = '3'
c = [23,7,34]
print("hello")
try:
    print(c[9])
    print(a/b)
except Exception as e:
    print(e)
except Exception as e:
    print(e)
print("India")

import pickle
try:
    file = open('student.dat','rb')
    while True:
        print(pickle.load(file))
except:
    pass
print("File ended!")

"""

#Day 14
#Map Reduce Filter
"""
Lambda map filtre reduce

#Lambda
square = lambda val:val*val
li = [1,2,3,4,5,6,7,8,9,10]

for x in li:
    print(square(x))

square = lambda val:val*2
li = [1,2,3,4,5,6,7,8,9,10]

for x in li:
    print(square(x))

short = lambda val:val[0:3]

li = ['January','February','March','April','May','June']
for month in li:
    print(short(month))
    
#map
short = lambda val:val[0:3]

li = ['January','February','March','April','May','June']
new = list(map(short,li))

print(new)

cube = lambda val:val**3

li=[1,2,3,4,5]

print(list(map(cube,li)))

capital = lambda str:str.upper()

li = ['hello','india','world','mumbai']
print(list(map(capital,li)))

li = [1,2,3,4,5]
print(list(map(lambda val:val**3,li)))

#Filter
li = [23,45,67,8,89,57,36,24,13,13,35,46,68,897,42]
print(list(filter(lambda x:x%2!=0,li)))

#Reduce
from functools import reduce
li = [x for x in range(1,11)]
print(reduce(lambda a,b:a+b,li))
"""

#Day 15
#POP :- Procedure Oriented Programming
#FOP :- Function Oriented Programming
#OOP :- Object Oriented Programming

"""
Four Main Pillars of OOp
-Class
-Object
-Encapulation
-Abstraction
-Inheritance
-Polymorphism
"""
#class,object
"""
Class :- It is a virtual enity and it is a blue print of object
Object :- It is a real world enity

syntax:
class class_name:
    class_properties

class myclass:
    myvar=(100)
    def myfun(self):
        print("I am from myclass",self.mycar)
"""

#Object    
'''
syntax
object_name = class_name()
object_name.class_properties()

obj = myclass()
obj.myfun()
'''

#Day 16
#Encapsulation
#Constructor : It is a functionality of a method, a method will automatically called when an object will be created. 
#A method is a constructor, if its name is__init__
#Destructor : Not Supported in Python. (C++ only)
'''
class Emp:
    #Variables
    empid = 101
    empname = 'Sakshi'
    empsal = 90000
    empcom = 'Google'
    #Methods
    def __init__(self):
        print("I am a constructor!")
    def displayEmp(self):
        print("Employee ID:",self.empid)
        print("Employee Name:",self.empname)
        print("Employee Salary:",self.empsal)
        print("Employee Company:",self.empcom)

emp1 = Emp()
emp1.displayEmp()
'''
'''
class Emp:
    empid = 0
    empname = ""
    empsal = 0
    empcom = "Google"
    #Data Shadowing
    @staticmethod
    def welcome():
        print("Welcome To Google")
    def __init__(self,empid,empname,empsal):
        self.empid = empid
        self.empname = empname
        self.empsal = empsal
    def displayEmp(self):
        print("Employee ID:",self.empid)
        print("Employee Name:",self.empname)
        print("Employee Salary:",self.empsal)
        print("Employee Company:",self.empcom)

emp1 = Emp(101,'Sakshi Yadav',100000)
emp1.welcome()
emp1.displayEmp()
emp2 = Emp(102,'Sanju yadav',84637)
emp2.displayEmp()
'''

#Day 17
#Inheritance
#Single inheritance
'''
class A:
    def fun1(self):
        print("I am Fun1 from class A")

class B(A):
    def fun2(self):
        print("I am fun2 from B")

obj = B()
obj.fun1()

#Mulitple inheritance
class A:
    def fun1(self):
        print("I am Fun1 from class A")

class B(A):
    def fun2(self):
        print("I am fun2 from B")

class C(B,A):
    def fun3(self):
        print("I am fun3 from class C")


obj = C()
obj.fun1()

#Multi-level inheritance
class A:
    def fun1(self):
        print("I am Fun1 from class A")

class B(A):
    def fun2(self):
        print("I am fun2 from B")

class C(B):
    def fun3(self):
        print("I am fun3 from class C")

obj = C()
obj.fun1()

#Hybrid inheritance
class A:
    def fun1(self):
        print("I am Fun1 from class A")

class B(A):
    def fun2(self):
        print("I am fun2 from B")

class C(A):
    def fun3(self):
        print("I am fun3 from class C")

class D(B,C):
    def fun4(self):
        print("I am fun4 from class D")
        
obj = D()
obj.fun3()

#Polymorphism(ploy[many] + morphism[Forms])

Types of Polymorphism
1.Runtime
-Function Overloading
-Function Overriding

2.Compile
-Operator Overloading
'''
'''
s = 'aman_kumar'
li = [2,3,4,5,67]
tu = (23,4,5,6,8)
se = {23,54,78,54,90}

print(max(s))
print(max(li))
print(max(tu))
print(max(se))

def add(x,y):
    return x+y

print(add(2,3))
print(add(2.3,3.2))
print(add('aman','kumar'))
print(add([23,4,5],[6,7,89]))
'''
'''
#Day 18
#Abstraction
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def fun1(self):
        print('It will be override')
    def fun2(self):
        print('I am from class A')

class B(A):
    def fun1(self):
        pass
    def fun3(self):
        print('I am from class B')
        
obj=B()
'''













