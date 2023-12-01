import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_report.txt'), "r")
inputtext = inputfile.readlines()

gam=""
eps=""

for index in range(len(inputtext[0].replace("\n", ""))):
    saver = []
    for line in inputtext:
        saver.append(line[index])
    most = str(max(set(saver), key=saver.count))
    least = str(abs(int(most)-1))
    gam = gam + most
    eps = eps + least
print("the power consumption is: " + str(int(gam, 2)*int(eps, 2)))

##stimmt nicht
def most_common(lst):
    return max(set(lst), key=lst.count)
def least_common(lst):
    return min(set(lst), key=lst.count)

saver = []
for line in inputtext:
    saver.append(line.replace("\n", ""))

for index in range(len(inputtext[0].replace("\n", ""))):

    temp=[]
    for element in saver:
        temp.append(element[index])
    most = most_common(temp)
    print("m", most)
    
    saver2= []
    for element in saver:
        if str(element[index]) == str(most):
            saver2.append(element)
    saver = saver2

    if len(saver) <= 1:
        o2_gen_rating = str(saver[0])
        print(o2_gen_rating)
        break

    

saver = []
for line in inputtext:
    saver.append(line.replace("\n", ""))

for index in range(len(inputtext[0].replace("\n", ""))):

    temp=[]
    for element in saver:
        temp.append(element[index])
    least = least_common(temp)
    print("l", least)
    
    saver2= []
    for element in saver:
        if str(element[index]) == str(least):
            saver2.append(element)
    saver = saver2

    if len(saver) <= 1:
        o2_scrub_rating = str(saver[0])
        print(o2_scrub_rating)
        break







print("life support rating: " + str(int(o2_gen_rating, 2)*int(o2_scrub_rating, 2)))