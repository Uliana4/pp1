import csv
with open("studentslist.csv", "r") as file:
    a=csv.DictReader(file)
    for row in a:
        if int(row["age"])<30:
            print(row["first_name"], end=" ")
            print(row["last_name"], end=" ")
            print(row["email"], end="\n")