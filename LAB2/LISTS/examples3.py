#Add list items
#1
thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)#Output:['apple', 'banana', 'cherry', 'orange']

#2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)#Output:['apple', 'orange', 'banana', 'cherry']

#3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)#Output:['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist)#Output:['apple', 'banana', 'cherry', 'kiwi', 'orange']





