"""
Rock: A, X
Paper: B, Y
Scissors: C, Z
"""

set_result = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

set_move = {
    ('draw', 'A'): 'X',
    ('win', 'A'): 'Y',
    ('lose', 'A'): 'Z',
    ('lose', 'B'): 'X',
    ('draw', 'B'): 'Y',
    ('win', 'B'): 'Z',
    ('win', 'C'): 'X',
    ('lose', 'C'): 'Y',
    ('draw', 'C'): 'Z'
}

points_for_result = {
    'win': 6,
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
        result = set_result[line[2]] #win/draw/lose
        points_from_outcome = points_for_result[result] #0/3/6

        condition = (result, line[0]) #[win/draw/lose, A/B/C]
        move = set_move[condition] #X/Y/Z
        points_from_choice = points_for_choice.index(move) + 1 #1/2/3

        points_from_round = points_from_choice + points_from_outcome
        overall_points += points_from_round

    return overall_points


file = setup('sample.txt')
points = calculate_score(file)
print('Overall points:', points)
