import json

book={
    "title":"Izara",
    "Year": 2021,
    "director":'Julia Dippel',
    "country":'Germany',
    "series":True
}

f=open("favourite.json", "w")
y =json.dumps(book, json_book, ident=4)

json_book.close()