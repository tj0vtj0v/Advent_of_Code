import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_fields.txt'), "r")
inputtext = inputfile.readlines()

number_order = inputtext[0].replace("\n", "").split(",")
inputtext = inputtext[2:]


games = []
game = []
for row in inputtext:
    if row == "\n":
        games.append(game)
        game = []
    else:
        line = []
        for number in row.split(" "):
            if len(number) >=1:
                line.append(number.replace("\n", ""))
        game.append(line)
        

        
def finder ():
    now_choosen = []
    for choosen in number_order:
        now_choosen.append(choosen)
        if len(now_choosen) <= 4:
            continue
        for game in games:
            bingo = False
            for line in game:
                choosen_count = 0
                for number in line:
                    if number in now_choosen:
                        choosen_count+=1
                if choosen_count == 5:
                    bingo = True
                
            for index in range(5):
                choosen_count = 0
                for line in game:
                    if line[index] in now_choosen:
                        choosen_count+=1
                if choosen_count == 5:
                    bingo = True
            if bingo:
                quersum = 0
                for line in game:
                    for number in line:
                        if number not in now_choosen:
                            quersum+=int(number)
                last = int(now_choosen[-1])
                return str(int(quersum*last))

print("final score = " + finder())


def last_finder ():
    now_choosen = []
    for choosen in number_order:
        now_choosen.append(choosen)
        if len(now_choosen) <= 4:
            continue
        for game in games:
            bingo = False
            for line in game:
                choosen_count = 0
                for number in line:
                    if number in now_choosen:
                        choosen_count+=1
                if choosen_count == 5:
                    bingo = True
                
            for index in range(5):
                choosen_count = 0
                for line in game:
                    if line[index] in now_choosen:
                        choosen_count+=1
                if choosen_count == 5:
                    bingo = True
            if bingo:
                if len(games) == 1:
                    quersum = 0
                    for line in game:
                        for number in line:
                            if number not in now_choosen:
                                quersum+=int(number)
                    last = int(now_choosen[-1])
                    return str(int(quersum*last))
                games.remove(game)


print("last final score = " + last_finder())
