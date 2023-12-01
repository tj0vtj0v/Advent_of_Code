import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_drivelog.txt'), "r")
inputtext = inputfile.readlines()

x=0
y=0
for vector in inputtext:
    direction = vector.split(" ")[0]
    value = vector.split(" ")[1].replace("\n", "")
    match direction:
        case "forward":
            x+=int(value)
        case "down":
            y+=int(value)
        case "up":
            y-=int(value)

print("the multiplied simple location is: " + str(x*y))




x=0
y=0
aim=0
for vector in inputtext:
    direction = vector.split(" ")[0]
    value = vector.split(" ")[1].replace("\n", "")
    match direction:
        case "forward":
            x+=int(value)
            y+=int(value)*aim
        case "down":
            aim+=int(value)
        case "up":
            aim-=int(value)

print("the multiplied complicated location is: " + str(x*y))
