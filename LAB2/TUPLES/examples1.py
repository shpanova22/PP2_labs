#Access Tuples

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])#Output:banana

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])#Output:cherry


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])#Output:('cherry', 'orange', 'kiwi')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[:4])#Output:('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])#Ouput:('cherry', 'orange', 'kiwi', 'melon', 'mango')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])#Output:('orange', 'kiwi', 'melon')

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")#Output:Yes, 'apple' is in the fruits tuple
  

