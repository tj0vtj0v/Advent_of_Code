import os
import msvcrt as m
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_hightmap.txt'), "r")
inputtext = inputfile.readlines()

#einmal jumpen 

map = []
height = 0
for line in inputtext:
    row = []
    line = line.removesuffix("\n")
    width = 0
    for char in line:
        row.append(char)
        width+=1
    map.append(row)
    height += 1

y_count = 0
for y in map:
    x_count = 0
    for x in y:
        if x == "S":
            start_y = y_count
            start_x = x_count
        elif x == "E":
            end_y = y_count
            end_x = x_count
        x_count+=1
    y_count+=1
del y_count, x_count, line, char, y, x, row#todebug


blob_edge =[[start_y, start_x]]
blob_body =[]
iterations = 0
while True:
    iterations+=1
    this_round = []
    for point in blob_edge:
        y = point[0]
        x = point[1]
        if map[y][x] == "S":  value = ord("a")
        else: value = ord(map[y][x])
        if map[y][x] == "E":
            print(iterations)
            break
    
        if x+1 < width:
          val2 = ord(map[y][x+1])-1
          if val2 == 121:
              val2 = 150
          coord = [y, (x+1)]
          if val2 <= value and coord not in blob_body and coord not in blob_edge:
              this_round.append([y, x+1])
              blob_body.append([y, x])
        if x > 0:
          val2 = ord(map[y][x-1])-1
          if val2 == 121:
              val2 = 150
          coord = [y, (x-1)]
          if val2 <= value and coord not in blob_body and coord not in blob_edge:
              this_round.append([y, x-1])
              blob_body.append([y, x])
        if y+1 < height:
          val2 = ord(map[y+1][x])-1
          if val2 == 121:
              val2 = 150
          coord = [(y+1), x]
          if val2 <= value and coord not in blob_body and coord not in blob_edge:
              this_round.append([y+1, x])
              blob_body.append([y, x])
        if y > 0:
          val2 = ord(map[y-1][x])-1
          if val2 == 121:
              val2 = 150
          coord = [(y-1), x]
          if val2 <= value and coord not in blob_body and coord not in blob_edge:
              this_round.append([y-1, x])
              blob_body.append([y, x])



    blob_edge = []
    for point in this_round:
        if point not in blob_edge:
            blob_edge.append(point)
    blob_body_new =[]
    for point in blob_body:
        if point not in blob_body_new:
            blob_body_new.append(point)
    blob_body = blob_body_new



    print(iterations)

    if iterations>=400:
      y_count = 0
      for y in map:
          x_count = 0
          for x in y:
              if [y_count, x_count] in blob_body:
                  print("#", end="")
              elif [y_count, x_count] in blob_edge:
                  print("=", end="")
              else:
                  print(x, end="")
              x_count+=1
          y_count+=1
          print()
      m.getch()
                

            

        
























#480 too high