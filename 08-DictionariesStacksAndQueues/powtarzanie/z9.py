countries = [
    {"name":"Poland", "population":40690016},
    {"name":"Litwa", "population":2800000},
    {"name":"Łotwa", "population":1884000},
    {"name":"Niemcy", "population":8300000},
    {"name":"Czechy", "population":200000}
]

i=0
while i<len(countries):
    # print(countries[i]["name"], countries[i]["population"])
    print(f'{countries[i]["name"]} {countries[i]["population"]}')
    i+=1