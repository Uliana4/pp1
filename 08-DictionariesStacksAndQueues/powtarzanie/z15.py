basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}


person = {
    **basic_data,
    **advanced_data
}

for x in person.items():
    print(x)