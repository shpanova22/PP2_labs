#A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")
print(thistuple) #Output:('apple', 'banana', 'cherry')

#Tuple items are ordered, unchangeable, and allow duplicate values.
#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Since tuples are indexed, they can have items with the same value:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)#Output:('apple', 'banana', 'cherry', 'apple', 'cherry')

thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))#Output:3

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))#Output:<class 'tuple'> <class 'str'>


