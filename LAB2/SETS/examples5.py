#Join Sets

'''There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.'''

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)#Output:{2, 'c', 'a', 3, 'b', 1}


#You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)#Output:{3, 1, 'b', 2, 'c', 'a'}



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)#Output:{cherry, 'b', 'a', banana, 'c', 1, Elena, John, 2, apple, 3}


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)#Output:{2, 3, cherry, 'b', apple, 1, 'a', John, Elena, 'c', banana}



#The union() method allows you to join a set with other data types, like lists or tuples.
#The result will be a set.

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)#Output:{'b', 3, 'c', 2, 1, 'a'}


#The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.


#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)  #Output:{2, 1, 'a', 'c', 'b', 3}


#Both union() and update() will exclude any duplicate items.


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)#Output:{'apple'}


#You can use the & operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)#Output:{'apple'}


#Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.


#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)#Output:{'apple'}


#The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}

set3 = set1.intersection(set2)
print(set3)#Output:{False, True, 'apple'}


set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)#Output:{'banana', 'cherry'}


#You can use the - operator instead of the difference() method, and you will get the same result.
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)#Output:{'banana', 'cherry'}


#Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.


#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)#Output:{'banana', 'cherry'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)#Output:{'google', 'banana', 'microsoft', 'cherry'}


#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)#Output:{'google', 'banana', 'microsoft', 'cherry'}


#Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)#Output:{'google', 'banana', 'microsoft', 'cherry'}








