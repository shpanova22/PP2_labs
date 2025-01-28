#Loop Lists

#1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) #Output:apple banana cherry
  
#2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) #Output: apple  banana cherry 
  
#3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 #Output:apple banana cherry
  
#4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] #Output: apple banana cherry






