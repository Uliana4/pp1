import json, csv

products_data=[]

with open("products.csv", "r") as file:
    a = csv.DictReader(file)
    for row in a:
        products_data.append(row)

with open("products.json", 'w') as f:
    b = json.dump(products_data, f)