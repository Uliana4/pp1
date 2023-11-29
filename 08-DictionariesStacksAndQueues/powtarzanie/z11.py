import json
movie = {
    "title":"Izara",
    "year": 2022,
    "actor":{"leading":"M.Sony","supporting":"A.Allience"},
    "oscar":False,
    "director":"M>K>J",
    "music":"Doremilala"
}
with open("json.json", "w") as file:
    # json.dump(movie, )