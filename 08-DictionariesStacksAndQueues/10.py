arr=[
    {"Country":"Poland", 'population':'114983403'},
    {"Country": "France",'population':"1412555151"},
    {"Country":"Germany",'population':"1301234"},
    {"Country":"Italy",'population':"23453645"},
    {"Country":"Spain",'popylation':"34636565"}
]

i=0
while i <len(arr): # pozwalia odczytywac cos w arr
    for k,w in arr[i].items():
     print(w, end=" ")
    print()   #zeby przeniesć na nast wiersz
    i+=1