import json

with open("data.json") as file:
    data = json.load(file)

# for key,value in data.items():
#     print(f"{key} : {value}")

i=0
while i<len(data):
    print(f'{data[i]} ')
    i+=1