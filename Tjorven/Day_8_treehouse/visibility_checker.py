import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_heightmap.txt'), "r")
inputmap = inputfile.readlines()

forest = []
for line in inputmap:
    line = line.removesuffix("\n")
    row = []
    for tree in line:
        row.append(tree)
    forest.append(row)


def check_left(line, index_of_row, tree):
    for previous in range(index_of_row):
        if line[previous] >= tree:
            return 1
    return 0

def check_right(line, index_of_row, tree):
    for following in range(len(line)-index_of_row-1):
        if line[following+index_of_row+1] >= tree:
            return 1
    return 0

def check_top(forest, index_of_row, index_of_line, tree):
    for previous in range(index_of_line):
        if forest[previous][index_of_row] >= tree:
            return 1
    return 0

def check_bottom(forest, index_of_row, index_of_line, tree):
    for following in range(len(forest)-index_of_line-1):
        if forest[following+index_of_line+1][index_of_row] >= tree:
            return 1
    return 0

visibilitymap = []
index_of_line = 0
total_visibility = 0
for line in forest:
    if index_of_line == 1:
        pass
    index_of_row = 0
    line_visibility = []
    for tree in line:
        invisible_counter = 0
        invisible_counter += check_left(line, index_of_row, tree)
        invisible_counter += check_right(line, index_of_row, tree)
        invisible_counter += check_top(forest, index_of_row, index_of_line, tree)
        invisible_counter += check_bottom(forest, index_of_row, index_of_line, tree)
        
        if invisible_counter == 4:
            line_visibility.append(" ")
        else:
            line_visibility.append(chr(240))
            total_visibility+=1
        index_of_row+=1
    visibilitymap.append(line_visibility)

    index_of_line+=1

print()
for line in visibilitymap:
    for tree in line:
        print(tree, end="")
    print()
print("\nvisible trees from outside: " + str(total_visibility))


def scenic_left(index_of_row,tree,line):
    view = 0
    for previous in range(index_of_row):
        view+=1
        if line[index_of_row-(previous+1)] >= tree:
            return view
    return view

def scenic_right(index_of_row,tree,line):
        view = 0
        for following in range(len(line)-index_of_row-1):
            view+=1
            if line[index_of_row+following+1] >= tree:
                return view
        return view

def scenic_top(index_of_line,index_of_row,tree,forest):
        view = 0
        for previous in range(index_of_line):
            view+=1
            if forest[index_of_line-(previous+1)][index_of_row] >= tree:
                return view
        return view

def scenic_bottom(index_of_line,index_of_row,tree,forest):
        view = 0
        for following in range(len(forest)-(index_of_line+1)):
            view+=1
            if forest[index_of_line + following + 1][index_of_row] >= tree:
                return view
        return view

index_of_line = 0
max_scenic_score = 0
for line in forest:
    if index_of_line == 1:
        pass
    index_of_row = 0
    for tree in line:
        scenic_score = 1
        scenic_score*=scenic_left(index_of_row,tree,line)
        scenic_score*=scenic_right(index_of_row,tree,line)
        scenic_score*=scenic_top(index_of_line,index_of_row,tree,forest)
        scenic_score*=scenic_bottom(index_of_line,index_of_row,tree,forest)

        if max_scenic_score < scenic_score:
            max_scenic_score = scenic_score
        index_of_row+=1
    index_of_line+=1

print("maximum scenic score: " + str(max_scenic_score))