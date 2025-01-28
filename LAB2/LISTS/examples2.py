#Change list items
#1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)#Output:['apple', 'blackcurrant', 'cherry']

#2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)#Output:['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

#3
thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)#Output:['apple', 'blackcurrant', 'watermelon', 'cherry']

#4
thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)#Output:['apple', 'watermelon']

#5
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)#Output:['apple', 'banana', 'watermelon', 'cherry']



