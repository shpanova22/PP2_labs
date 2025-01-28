#Remove List Items

#1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)#Output:['apple', 'cherry']

#2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)#Output:['apple', 'cherry', 'banana', 'kiwi']
#(If there are more than one item with the specified value, the remove() method removes the first occurrence)


#3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)#Output:['apple', 'cherry']

#4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)#Output:['apple', 'banana']

#5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)#Output:['banana', 'cherry']

#6
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".

#7
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #Output:[]




