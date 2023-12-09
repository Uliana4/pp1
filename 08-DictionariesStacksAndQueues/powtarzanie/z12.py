import json
student = {
    "name":"Izara",
    "surnamer": "Bochniak",
    "visuality":{"eyes":"green", "hair":"blond", "vaste":57},
    "nr_albumu":223456,
    "is_srudent":True,
    "year":2022,
    "is_graduate":False
}

with open("student.json", "w")  as file:
    json.dump(student, file)

