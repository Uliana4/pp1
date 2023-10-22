speed = int(input("Enter the car speed: "))
speed_limit_min = 40
speed_limit_max = 140
if speed > speed_limit_max or speed < speed_limit_min:
    print("Warning: invalid car speed !!!")
else:
    print("OK")