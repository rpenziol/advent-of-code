# https://adventofcode.com/2022/day/2
import common

input = common.read_file(day='02', type='final')

rounds = input.strip().split('\n')

rock = {
    'name': 'rock',
    'score': 1,
    'beats': 'scissors',
    'lose': 'paper'
}
paper = {
    'name': 'paper',
    'score': 2,
    'beats': 'rock',
    'lose': 'scissors'
}
scissors = {
    'name': 'scissors',
    'score': 3,
    'beats': 'paper',
    'lose': 'rock'
}

guide = {
    'A': rock,
    'B': paper,
    'C': scissors,
    'X': rock,
    'Y': paper,
    'Z': scissors,
}

my_total = 0

for round in rounds:
    opponent_choice, my_choice = round.split(' ')

    opponent_choice = guide[opponent_choice]
    my_choice = guide[my_choice]

    if opponent_choice['name'] == my_choice['name']: # Draw
        score = my_choice['score'] + 3
    elif opponent_choice['name'] == my_choice['beats']: # I win
        score = my_choice['score'] + 6
    elif opponent_choice['beats'] == my_choice['name']: # I lose
        score = my_choice['score'] + 0

    my_total += score

print(my_total)  # Part 1

choices = {
    'rock': rock,
    'paper': paper,
    'scissors': scissors
}

my_total = 0

for round in rounds:
    opponent_choice, game_outcome = round.split(' ')

    opponent_choice = guide[opponent_choice]

    if game_outcome == 'Y': # Draw
        my_choice = choices[opponent_choice['name']]
        score = my_choice['score'] + 3
    elif game_outcome == 'Z': # I win
        my_choice = choices[opponent_choice['lose']]
        score = my_choice['score'] + 6
    elif game_outcome == 'X': # I lose
        my_choice = choices[opponent_choice['beats']]
        score = my_choice['score'] + 0

    my_total += score

print(my_total)  # Part 2
