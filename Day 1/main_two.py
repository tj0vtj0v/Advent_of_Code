current_sum = 0
sum_collection = []


def setup(f):
    file = open(f, 'r')
    return file


def analyse_line(file, all: list, current: int) -> list:
    for line in file:
        if line == "\n":
            all.append(current)
            current = 0
        else:
            line = line[0: -1]
            current += int(line)
    all.append(current)
    return all

def find_highest(sums: list) -> int:
    highest = sums[0]
    for element in sums:
        if element > highest:
            highest = element
    return highest

def find_top_three(sums: list) -> int:
    sorted_sums = sorted(sums)
    top_three = sorted_sums[-3:]
    top_three_sum = 0
    for x in top_three:
        top_three_sum += x
    return top_three_sum

file = setup('sample.txt')
all_sums = analyse_line(file, sum_collection, current_sum)
#highest = find_highest(all_sums)
#print('The highest calories are:', highest)
highest_three = find_top_three(all_sums)
print('The sum of the top 3 is:', highest_three)
