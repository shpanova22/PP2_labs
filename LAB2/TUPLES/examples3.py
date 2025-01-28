#Unpack Tuples
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red) #Output:apple banana cherry


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)#Output:apple banana ['cherry', 'strawberry', 'raspberry']


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)#Output:apple ['mango', 'papaya', 'pineapple'] cherry


