import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_calorines.txt'), "r")
inputtext = inputfile.readlines()

calorines = 0
resultlist = []
for line in inputtext:
    linetext = line.replace("\n", "")
    if linetext != "":
        calorines += int(linetext)
    else: 
        resultlist.append(calorines)
        calorines = 0

resultlist.sort()
print("most calorines: " + str(resultlist[-1]))

all = 0
for most in resultlist[-3:]:
    all += int(most)

print("calorines of top 3: " + str(all))