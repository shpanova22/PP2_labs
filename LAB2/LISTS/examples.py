#1
thislist = ["apple", "banana", "cherry"]
print(thislist) #Output:['apple', 'banana', 'cherry']

#2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)#Output:["apple", "banana", "cherry", "apple", "cherry"]

#3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))#Output:3

#4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)#Output:['apple', 'banana', 'cherry'][1, 5, 7, 9, 3][True, False, False]

#5
list1 = ["abc", 34, True, 40, "male"]

print(list1)#Output:['abc', 34, True, 40, 'male']

#6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))#Output:<class 'list'>

#7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) #Output: ['apple', 'banana', 'cherry'] (Using the list() constructor to make a List)

'''Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.'''





