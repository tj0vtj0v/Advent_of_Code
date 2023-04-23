import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_ventmap.txt'), "r")
inputtext = inputfile.readlines()

vents = []
for lines in inputtext:
    lines = lines.removesuffix("\n")
    coordinate_pair = []
    for handle in lines.split(" -> "):
        coordinate_pair.append(handle.split(","))
    vents.append(coordinate_pair)

#frame (0|0)->(1000|1000)

danger = []
danger2 = []
for vent in vents:
    x1 = int(vent[0][0])
    y1 = int(vent[0][1])
    x2 = int(vent[1][0])
    y2 = int(vent[1][1])

    if x1 == x2:
        if y2 >= y1:
            for y in range(y2-y1+1):
                danger.append([x1, y+y1])
                danger2.append(str(x1) + "," + str(y+y1))
        elif y2 < y1:
            for y in range(y1-y2+1):
                danger.append([x1, y+y2])
                danger2.append(str(x1) + "," + str(y+y2))
    elif y1 == y2:
        if x2 >= x1:
            for x in range(x2-x1+1):
                danger.append([x+x1, y1])
                danger2.append(str(x+x1) + "," + str(y1))
        elif x2 < x1:
            for x in range(x1-x2+1):
                danger.append([x+x2, y1])
                danger2.append(str(x+x2) + "," + str(y1))
    else:
        if y2 >= y1:
            if x2 >= x1:
                for c in range(x2-x1+1):
                    danger.append([c+x1, y1+c])
                    danger2.append(str(c+x1) + "," + str(y1+c))
            elif x2 < x1:
                for c in range(x1-x2+1):
                    danger.append([c+x2, y1+c])
                    danger2.append(str(c+x2) + "," + str(y1+c))
        elif y2 < y1:
            if x2 >= x1:
                for c in range(x2-x1+1):
                    danger.append([c+x1, y2+c])
                    danger2.append(str(c+x1) + "," + str(y2+c))
            elif x2 < x1:
                for c in range(x1-x2+1):
                    danger.append([c+x2, y2+c])
                    danger2.append(str(c+x2) + "," + str(y2+c))


#long runtime but works
danger_spots = list(set(danger2))
double_danger_spots = []
for spot in danger2:
    if spot in danger_spots:
        danger_spots.remove(spot)
    elif spot not in double_danger_spots:
        double_danger_spots.append(spot)
#print(len(set(double_danger_spots)))






