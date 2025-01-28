#Sort Lists
#1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)#Output:['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#2
thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)#Output:[23, 50, 65, 82, 100]

#3
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)#Output:['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#4
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)#Output:[100, 82, 65, 50, 23]

#5
#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)#Output: [50, 65, 23, 82, 100] 
#You can also customize your own function by using the keyword argument key = function.
#The function will return a number that will be used to sort the list (the lowest number first)

#6
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist)#Output:['Kiwi', 'Orange', 'banana', 'cherry']

#7
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)#Output:['banana', 'cherry', 'Kiwi', 'Orange']

#8
#What if you want to reverse the order of a list, regardless of the alphabet?
#The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist)#Output:['cherry', 'Kiwi', 'Orange', 'banana']







