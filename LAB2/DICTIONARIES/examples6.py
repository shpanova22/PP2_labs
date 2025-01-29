#Copy a dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)#Output:{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)#Output:{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}




