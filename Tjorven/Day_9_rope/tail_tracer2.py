import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_movement.txt'), "r")
inputmovement = inputfile.readlines()

dirmove = []
for move in inputmovement:
    move = move.removesuffix("\n")
    dirmove.append(move.split(" "))

#get first knot movement
head_position_per_move = ["0.0;0.0"]
for move in dirmove:
    for distance in range(int(move[1])):
        xhead = float(head_position_per_move[-1].split(";")[0])
        yhead = float(head_position_per_move[-1].split(";")[1])
        if yhead == 0:
            yhead = 0.0
        if xhead == 0:
            xhead = 0.0

        direction = move[0]
        if direction == "R":
            xhead+=1
        if direction == "L":
            xhead-=1
        if direction == "U":
            yhead+=1
        if direction == "D":
            yhead-=1
        head_position_per_move.append(str(xhead) + ";" + str(yhead))

#extend next knots movement array from movement of previous knot
def follow_pos_calc(xhead, yhead, follower_position_per_move:list[str]):
    xtail = float(follower_position_per_move[-1].split(";")[0])
    ytail = float(follower_position_per_move[-1].split(";")[1])

    xdist = float(xhead-xtail)
    ydist = float(yhead-ytail)
    if abs(xdist) > 1:
        xtail += xdist/2
        if abs(ydist) > 1:
            ytail += ydist/2
        elif abs(ydist) > 0:
            ytail += ydist
    elif abs(ydist) > 1:
        ytail += ydist/2
        if abs(xdist) > 1:
            xtail += xdist/2
        elif abs(xdist) > 0:
            xtail += xdist
    if ytail == 0:
        ytail = 0.0
    if xtail == 0:
        xtail = 0.0
    follower_position_per_move.append(str(round(xtail, 0)) + ";" + str(round(ytail, 0)))
    return follower_position_per_move

#get next knots movement
def calc_next_knot(full_leader_position_per_move):
    follower_position_per_move = ["0.0;0.0"]
    counter = 0
    for move in full_leader_position_per_move:
        xhead = float(move.split(";")[0])
        yhead = float(move.split(";")[1])
        follower_position_per_move = follow_pos_calc(xhead, yhead, follower_position_per_move)
        counter+=1
    return follower_position_per_move[1:]

#simulate knot movement based on previous knot movement
def simulator(knots, full_leader_position_per_move):
    count = 1
    while count < knots:
        last_knot_position_per_move = calc_next_knot(full_leader_position_per_move)
        full_leader_position_per_move = last_knot_position_per_move
        #print(count+1, "knots:", len(set(last_knot_position_per_move))) ##for help
        for move in last_knot_position_per_move:
            for pos in move.split(";"):
                if ".0" not in pos:
                    return last_knot_position_per_move
        count+=1
    print("with", knots, "knots the last knot visited", len(set(last_knot_position_per_move)), "positions.")
    return last_knot_position_per_move

#start simulation with 2 knots -> 1 iterations --> works
knots = 2
last_knot_position_per_move = simulator(knots, head_position_per_move)

#start simulation with 10 knots -> 9 iterations --> doesnt work ---> fuck that shit
knots = 10
last_knot_position_per_move = simulator(knots, head_position_per_move)
print("last is wrong")


#2774 too high
#2624 too high
#2613 too hight
            
#2433 too low
