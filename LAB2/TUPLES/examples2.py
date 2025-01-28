#Update Tuples

#You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)#Output:("apple", "kiwi", "cherry")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)#Output:('apple', 'banana', 'cherry', 'orange')


#Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)#Output:('apple', 'banana', 'cherry', 'orange')


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)#Output:('banana', 'cherry')

#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists




 