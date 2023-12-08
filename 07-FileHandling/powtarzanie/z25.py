import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
sum = 0
count=0
for i in temperatures:
    sum+=int(i)
    count+=1
print(sum//count)

# sum = int(temperatures[0])+int(temperatures[1])+int(temperatures[2])
# print(sum)