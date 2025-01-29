#A set is a collection which is unordered, unchangeable*, and unindexed.

#* Note: Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset)#Output:{'apple', 'cherry', 'banana'}

#Note: the set list is unordered, meaning: the items will appear in a random order.

#Set items are unordered, unchangeable, and do not allow duplicate values.

#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

#Set items are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)#Output:{'banana', 'cherry', 'apple'}



#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)#Output:{True, 2, 'banana', 'cherry', 'apple'}


#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)#Output:{False, True, 'cherry', 'apple', 'banana'}


thisset = {"apple", "banana", "cherry"}

print(len(thisset))#Output:3


myset = {"apple", "banana", "cherry"}

print(type(myset))#Output:<class 'set'>







