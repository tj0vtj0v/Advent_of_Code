import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_measurment.txt'), "r")
inputtext = inputfile.readlines()

old_height = inputtext[0]
increase_counter = 0
for height in inputtext:
    if int(old_height) < int(height):
        increase_counter+=1
    old_height = height
print("the direct climbingcount is: " + str(increase_counter))


height_4 = inputtext[0]
height_3 = inputtext[1]
height_2 = inputtext[2]
height_1 = inputtext[3]
increase_counter = 1
counter = 1
for height in inputtext:
    if counter >= 4:
        if int(height_3)+int(height_2)+int(height_1) > int(height_4)+int(height_3)+int(height_2):
            increase_counter+=1
        height_4=height_3
        height_3=height_2
        height_2=height_1
        height_1=height
    counter+=1
print("the over 3 average climbingcount is: " + str(increase_counter))