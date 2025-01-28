#Access list items
#1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])#Output:banana

#2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])#Output:cherry

#3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#Output:['cherry', 'orange', 'kiwi']

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

#4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])#Output:['apple', 'banana', 'cherry', 'orange']

#This will return the items from index 0 to index 4.

#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included 

#5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])#Output:['cherry', 'orange', 'kiwi', 'melon', 'mango']

#This will return the items from index 2 to the end.

#Remember that index 0 is the first item, and index 2 is the third

#6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])#Output:['orange', 'kiwi', 'melon']

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1

#7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")#Output:Yes, 'apple' is in the fruits list
  
  
