#Add Set Items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) #Output:{'cherry', 'orange', 'apple', 'banana'}


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)#Output:{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}


#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)#Output:{'banana', 'cherry', 'apple', 'orange', 'kiwi'}


