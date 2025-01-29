#Access items

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)#Output:Mustang

#There is also a method called get() that will give you the same result:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)#Output:Mustang


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)#Output:dict_keys(['brand', 'model', 'year'])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change #Output:dict_keys(['brand', 'model', 'year']) dict_keys(['brand', 'model', 'year', 'color'])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)#Output:dict_values(['Ford', 'Mustang', 1964])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change #Output:dict_values(['Ford', 'Mustang', 1964]) dict_values(['Ford', 'Mustang', 2020])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)#output:dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change #Output:dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]) dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change #Output:dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]) dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") #Output:Yes, 'model' is one of the keys in the thisdict dictionary
