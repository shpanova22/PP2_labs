#Change items

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)#Output:{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)#Output:{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}



