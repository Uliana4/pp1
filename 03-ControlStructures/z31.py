x = int(input("Enter the x: "))
y = int(input("Enter the y: "))

if x>0 and y>0:
    quadrant = "first" 
    print(f"Point P{x, y} is in the {quadrant} quadrant of the coordinate system")

elif x>0 and y<0 :
    quadrant = "forth"
    print(f"Point P{x, y} is in the {quadrant} quadrant of the coordinate system")

elif x<0 and y>0:
    quadrant = "second"
    print(f"Point P{x, y} is in the {quadrant} quadrant of the coordinate system")

elif x<0 and y<0:
    quadrant = "third"
    print(f"Point P{x, y} is in the {quadrant} quadrant of the coordinate system")

elif y==0 and (x > 0 or x <0):
    print(f"Point P{x, y} is located on X axis") 

elif x==0 and (y >0 or y<0):
    print(f"Point P{x, y} is located on Y axis") 

elif x == 0 and y == 0:
    quadrant = "(0,0)"
    print(f"Point P{x, y} is located in the position (0,0)")