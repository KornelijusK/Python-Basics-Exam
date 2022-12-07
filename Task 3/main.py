# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def showObjectKeys():

  audi_list = []

  for i in audi.values():
    audi_list.append(i)

  print(audi_list)
  print(type(audi_list))

showObjectKeys()



