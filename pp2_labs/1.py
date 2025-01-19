#PYTHON HOME; INTRO; GET STARTED 
print("Hello,world!")

#PYTHON SYNTAX
if 5 > 2:
  print("Five is greater than two!") #output:Five is greater than two!
  
#if 5 > 2:
#print("Five is greater than two!") #output:Error

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") #outpit:Five is greater than two! Five is greater than two!

#if 5 > 2:
 #print("Five is greater than two!")
        #print("Five is greater than two!")#output:Error
        
#PYTHON COMMENTS
#This is a comment
print("Hello, World!") #output:Hello,World!

#PYTHON VARIABLES
x = 5
y = "John"
print(x)
print(y) #output:5 John

x = 4       # x is of type int          
x = "Sally"  # x is now of type str
print(x) #output: Sally


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#output: 3 3 3.0

x = 5
y = "John"
print(type(x))
print(type(y))  #output: <class 'int'> <class 'str'>

x = "John"
# is the same as
x = 'John' #output: John John

a = 4
A = "Sally"
#A will not overwrite a  

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" #output: John(6)

#2myvar = "John"
#my-var = "John"
#my var = "John" #This example will produce an error in the result

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z) #output: Orange Banana Cherry

x = y = z = "Orange"
print(x)
print(y)
print(z) #output: Orange Orange Orange

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z) #output: apple banana cherry

x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #output: Python is awesome 

x = 5
y = 10
print(x + y)  #output: 15

#x = 5
#y = "John"
#print(x + y) #output:Error 

x = 5
y = "John"
print(x, y) #output: 5 John 

#GLOBAL VARIABLE 
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() #output: Python is awesome


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) #output: Python is fantastic Python is awesome (If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #output:Python is fantastic (If you use the global keyword, the variable belongs to the global scope:)



x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #output:Python is fantastic


#PYTHON DATA TYPES
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType 


x = 5
print(type(x)) #output:<class 'int'>

x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset

#PYTHON NUMBERS

x = 1    # int
y = 2.8  # float
z = 1j   # complex

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z)) # output: <class 'int'> <class 'int'> <class 'int'>

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z)) #output: <class 'float'> <class 'float'> <class 'float'>


x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z)) #output: <class 'complex'> <class 'complex'> <class 'complex'>

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z)) #output:1.0 2 (1+0j) <class 'float'> <class 'int'> <class 'complex'>

#Note: You cannot convert complex numbers into another number type.

import random

print(random.randrange(1, 10)) #output:4

#PYTHON STRINGS

a = "Hello, World!"
print(a[1]) #output: e

for x in "banana":
  print(x) #output: b a n a n a
  
a = "Hello, World!"
print(len(a)) #output:13

txt = "The best things in life are free!"
print("free" in txt) #output: True

txt = "The best things in life are free!"
print("expensive" not in txt)#output: True

#SLICING
b = "Hello, World!"
print(b[2:5]) #output:llo

b = "Hello, World!"
print(b[:5]) #output:Hello

b = "Hello, World!"
print(b[2:]) #output:llo, World!

b = "Hello, World!"
print(b[-5:-2]) #output:orl

#MODIFY STRINGS

a = "Hello, World!"
print(a.upper()) #output:HELLO, WORLD!

a = "Hello, World!"
print(a.lower()) #output: hello, world!

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J")) #output: Jello, World!

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#FORMAT STRINGS
age = 36
txt = f"My name is John, I am {age}"
print(txt) #output:My name is John, I am 36

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #output:The price is 59.00 dollars

txt = f"The price is {20 * 59} dollars"
print(txt) #output:The price is 1180 dollars

#ESCAPE CHARACTERS
txt = "We are the so-called \"Vikings\" from the north."
print(txt) #output:We are the so-called "Vikings" from the north.



























