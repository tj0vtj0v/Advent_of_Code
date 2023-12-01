import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_threads.txt'), "r")
inputtext = inputfile.readlines()

commands:list[str] = []
for line in inputtext:
    linetext = line.removesuffix("\n")
    commands.append(linetext)

cycles = []
x_value = 1
for commad in commands:
    if commad == "noop":
        cycles.append(x_value)
    elif "addx" in commad:
        cycles.append(x_value)
        cycles.append(x_value)
        x_value += int(commad.split(" ")[1])

counter = 1
wanted = 0
line = 0
print("\nCRT Display:\n ________________________________________\n|", end="")
for x_value in cycles:
    #task 1
    if counter == 20: wanted+=counter*int(x_value)
    if counter == 60: wanted+=counter*int(x_value)
    if counter == 100: wanted+=counter*int(x_value)
    if counter == 140: wanted+=counter*int(x_value)
    if counter == 180: wanted+=counter*int(x_value)
    if counter == 220: wanted+=counter*int(x_value)
    
    #task 2
    pixelind = (counter-1)-(line*40)
    if abs(pixelind-x_value) <= 1:
        print("#", end="")
    else: 
        print(" ", end="")
    if counter%40 == 0:
        print("|\n|", end="")
        line+=1
    
    counter+=1

print("________________________________________|\n\nsignal strebgth sum = " + str(wanted))


