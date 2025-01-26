#Evaluate Values and Variables
#1
print(bool("Hello"))
print(bool(15)) #Output: True True

#2
x = "Hello"
y = 15

print(bool(x))
print(bool(y))#Output: True True

'''Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

Example ''' 
#3
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"])) #Output: True True True

#4
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({})) #Output: False False False False False False False 

#BUT
print(bool(" ")) #Output: True

#5
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #Output: False

#6
def myFunction() :
  return True

print(myFunction())#Output: True

#7
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")#Output: YES!
  
#7
x = 200
print(isinstance(x, int)) #Output: True






