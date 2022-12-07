import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_ranges.txt'), "r")
inputtext = inputfile.readlines()

fullycontained = 0
contained = 0
for line in inputtext:
    linetext = line.replace("\n", "")
    range1 = linetext.split(",")[0]
    range2 = linetext.split(",")[1]
    range1_min = int(range1.split("-")[0])
    range1_max = int(range1.split("-")[1])
    range2_min = int(range2.split("-")[0])
    range2_max = int(range2.split("-")[1])
    if (range1_min <= range2_min and range1_max >= range2_max) or (range2_min <= range1_min and range2_max >= range1_max):
        fullycontained += 1
    if (range1_min <= range2_min and range1_max >= range2_min) or (range2_min <= range1_min and range2_max >= range1_min):
        contained += 1
print(str(fullycontained) + " ranges are fully contained\n" + str(contained) + " ranges are containd in eachother")