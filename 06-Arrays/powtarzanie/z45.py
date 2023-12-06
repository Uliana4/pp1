import matplotlib.pyplot as plt
import math

x=[]
y=[]

for n in range(0, 361):
    x.append(n)
    x_rad = [math.radians(angle) for angle in x]

for n in x:
    y=[math.sin(angle) for angle in x_rad]

plt.plot(x,y)
plt.xlabel('degrees')
plt.ylabel('y=sin(x)')
plt.title("Graph of sin(x)")
plt.grid(True)
plt.show()