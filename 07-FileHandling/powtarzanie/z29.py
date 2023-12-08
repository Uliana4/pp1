import re
with open("grades.txt", 'r') as f:
    a = f.read()
    ocena = re.findall(r'\d.{2}', a)
    sum = 0
    for i in ocena:
        sum+=float(i)
print(round(sum/len(ocena)), 1)