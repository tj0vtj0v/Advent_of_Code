"""
Rock: A, X
Paper: B, Y
Scissors: C, Z
"""

windrawlose = {
    'AX': 'draw',
    'AY': 'win',
    'AZ': 'lose',
    'BX': 'lose',
    'BY': 'draw',
    'BZ': 'win',
    'CX': 'win',
    'CY': 'lose',
    'CZ': 'draw'
}

points_for_result = {
    'win' : 6,
    'draw': 3,
    'lose': 0
}

points_for_choice = ['X', 'Y', 'Z']


def setup(f):
    file = open(f, 'r')

    return file

def calculate_score(file) -> int:
    overall_points = 0
    for line in file:
        relation = line[0] + line[2]
        outcome = windrawlose[relation]
        points_from_outcome = points_for_result[outcome]
        points_from_choice = points_for_choice.index(line[2]) + 1
        points_from_round = points_from_choice + points_from_outcome
        overall_points += points_from_round

    return overall_points

file = setup('sample.txt')
points = calculate_score(file)
print('Overall points:', points)