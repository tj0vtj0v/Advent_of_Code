import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_movement.txt'), "r")
inputtext = inputfile.readlines()

positions = [['N', 'W', 'F', 'R', 'Z', 'S', 'M', 'D'], ['S', 'G', 'Q', 'P', 'W'], ['C', 'J', 'N', 'F', 'Q', 'V', 'R', 'W'], ['L', 'D', 'G', 'C', 'P', 'Z', 'F'], ['S', 'P', 'T'], ['L', 'R', 'W', 'F', 'D', 'H'], ['C', 'D', 'N', 'Z'], ['Q', 'J', 'S', 'V', 'F', 'R', 'N', 'W'], ['V', 'W', 'Z', 'G', 'S', 'M', 'R']]

for line in inputtext:
    linetext = line.replace("\n", "")
    quantity, source, target = int(linetext.split(" ")[1]), int(linetext.split(" ")[3])-1, int(linetext.split(" ")[5])-1
    while quantity > 0:
        value = positions[source][0]
        positions[source].remove(value)
        positions[target].reverse()
        positions[target].append(value)
        positions[target].reverse()
        quantity -= 1

toplayer = ""
for x in positions:
    toplayer = toplayer + x[0]
print("carry one at once: " + toplayer)

positions = [['N', 'W', 'F', 'R', 'Z', 'S', 'M', 'D'], ['S', 'G', 'Q', 'P', 'W'], ['C', 'J', 'N', 'F', 'Q', 'V', 'R', 'W'], ['L', 'D', 'G', 'C', 'P', 'Z', 'F'], ['S', 'P', 'T'], ['L', 'R', 'W', 'F', 'D', 'H'], ['C', 'D', 'N', 'Z'], ['Q', 'J', 'S', 'V', 'F', 'R', 'N', 'W'], ['V', 'W', 'Z', 'G', 'S', 'M', 'R']]

for line in inputtext:
    linetext = line.replace("\n", "")
    quantity, source, target = int(linetext.split(" ")[1]), int(linetext.split(" ")[3])-1, int(linetext.split(" ")[5])-1
    value = positions[source][0:quantity]
    value.reverse()
    for ind in range(quantity):
      positions[source].pop(0)
    positions[target].reverse()
    for thing in value:
        
        positions[target].append(thing)
    positions[target].reverse()

toplayer = ""
for x in positions:
    toplayer = toplayer + x[0]
print("carry multiple at once: " + toplayer)