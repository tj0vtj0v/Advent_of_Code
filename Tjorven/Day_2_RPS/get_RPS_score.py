import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_RPS.txt'), "r")
inputtext = inputfile.readlines()

scores_2 = []
scores_1 = []
for line in inputtext:
    score_1 = 0
    score_2 = 0
    linetext = line.replace("\n", "")
    other = linetext[0]
    you = linetext[-1]
    match you:
        case "X":#rock
            score_1 +=1
            match other:
                case "A":#rock
                    score_1 +=3
                case "B":#paper
                    score_1 +=0
                case "C":#scissors
                    score_1 +=6
        case "Y":#paper
            score_1 +=2
            match other:
                case "A":#rock
                    score_1 +=6
                case "B":#paper
                    score_1 +=3
                case "C":#scissors
                    score_1 +=0
        case "Z":#scissors
            score_1 +=3
            match other:
                case "A":#rock
                    score_1 +=0
                case "B":#paper
                    score_1 +=6
                case "C":#scissors
                    score_1 +=3
    scores_1.append(score_1)
    
    match you:
        case "X":#loose
            score_2 +=0
            match other:
                case "A":#rock
                    score_2 +=3
                case "B":#paper
                    score_2 +=1
                case "C":#scissors
                    score_2 +=2
        case "Y":#draw
            score_2 +=3
            match other:
                case "A":#rock
                    score_2 +=1
                case "B":#paper
                    score_2 +=2
                case "C":#scissors
                    score_2 +=3
        case "Z":#win
            score_2 +=6
            match other:
                case "A":#rock
                    score_2 +=2
                case "B":#paper
                    score_2 +=3
                case "C":#scissors
                    score_2 +=1
    scores_2.append(score_2)

result = 0
for round in scores_1:
    result += int(round)
print("if you apply RPS values to XYZ you score " + str(result) + " points")
result = 0
for round in scores_2:
    result += int(round)
print("if you apply W/L/D values to XYZ you score " + str(result) + " points")


