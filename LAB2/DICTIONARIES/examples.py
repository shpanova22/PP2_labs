thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)#Output:{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#Dictionary items are ordered, changeable, and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])#output:Ford

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)#Output:{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))#Output:3


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)#Output:{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))#Output:<class 'dict'>


thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict)#Output:{'name': 'John', 'age': 36, 'country': 'Norway'}







