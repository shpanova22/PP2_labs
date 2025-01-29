#Remove set items

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) #Output:{'cherry', 'apple'}



thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)#Output:{'apple', 'cherry'}



#Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal  Output:banana {'cherry', 'apple'}


#The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)#Uutput:set()


#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) #this will raise an error because the set no longer exists



