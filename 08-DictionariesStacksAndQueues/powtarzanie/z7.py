person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

# a
for x, y in person.items():
  print(x, y)
# b
person["name"]
# c
person["hobby"]
# d
person["surname"]="Nowak"
# e
person["married"]=not person["married"]
# f
person["gender"]='male'
# g
person["hobby"]=person["hobby"]+['bicycle'] 
# person["hobby"].append('bicycle')
# h
# person.update({"phone": "313131444"})
person["phone"]["work"]="313131444"

for x, y in person.items():
  print(x, y)