import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
relation = []
prio_count = 1
for letter in lower:
    relation.append((letter, prio_count))
    prio_count += 1
for letter in upper:
    relation.append((letter, prio_count))
    prio_count += 1

import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_rucksack.txt'), "r")
inputtext = inputfile.readlines()

priolist=[]
for line in inputtext:
    prio = 0
    linetext = line.replace("\n", "")
    left_comp = linetext[0:int((len(linetext)/2))]
    right_comp = linetext.replace(left_comp, "")
    for left_item in left_comp:
        for right_item in right_comp:
            if left_item == right_item:
                for element in relation:
                    if left_item == element[0]:
                        prio = element[1]
            right_comp.replace(right_item, "")
    priolist.append(prio)

sum = 0
for prio in priolist:
    sum += int(prio)

print("prio sum = " + str(sum))

grouper = 0
groups = []
group = []
for line in inputtext:
    linetext = line.replace("\n", "")
    group.append(linetext)
    grouper += 1
    if grouper >= 3:
        groups.append(group)
        group = []
        grouper = 0

badgeprio = []

for group in groups:
    check = True
    member1 = group[0]
    member2 = group[1]
    member3 = group[2]
    for a in member1:
        for b in member2:
              for c in member3:
                  if a == b == c and check:
                      check = False
                      for element in relation:
                          if a == element[0]:
                              badgeprio.append(element[1])
badgepriosum = 0
for prio in badgeprio:
    badgepriosum += int(prio)
print("badgeprio sum = " + str(badgepriosum))