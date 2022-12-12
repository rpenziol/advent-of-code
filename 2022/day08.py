# https://adventofcode.com/2022/day/8
import numpy
import common

input = common.read_file(day='08', type='final')

input_rows = input.strip().split('\n')

rows = []

for row in input_rows:
    rows.append([*row])

matrix = numpy.array(rows)

num_rows = len(numpy.array(rows)[:, 0])
num_columns = len(numpy.array(rows)[0, :])

visible_count = 0

for row in range(num_rows):
    for column in range(num_columns):
        if row == 0 or row == num_rows-1:
            visible_count+=1
            continue
        if column == 0 or column == num_columns-1:
            visible_count+=1
            continue

        tree_height = matrix[row, column]

        if max(matrix[row, column+1:]) < tree_height: # Visible right
            visible_count+=1
            continue

        if max(matrix[row, :column]) < tree_height: # Visible left
            visible_count+=1
            continue

        if max(matrix[row+1:, column]) < tree_height: # Visible bottom
            visible_count+=1
            continue

        if max(matrix[:row, column]) < tree_height: # Visible top
            visible_count+=1
            continue

print(visible_count)  # Part 1


top_scenic_score = 0

def visible_trees(treehouse_height, trees):
    visible_tree = []

    for tree in trees:
        tree_height = int(tree)

        visible_tree.append(tree_height)

        if tree_height >= treehouse_height:
            break

    return visible_tree


for row in range(num_rows):
    for column in range(num_columns):
        if row == 0 or column == 0:
            continue

        treehouse_height = int(matrix[row, column])

        visible_right = visible_trees(treehouse_height, matrix[row, column+1:])
        visible_left = visible_trees(treehouse_height, reversed(matrix[row, :column]))
        visible_bottom = visible_trees(treehouse_height, matrix[row+1:, column])
        visible_up = visible_trees(treehouse_height, reversed(matrix[:row, column]))

        total_scenic_score = len(visible_right) * len(visible_left) * len(visible_bottom) * len(visible_up)

        if total_scenic_score > top_scenic_score:
            top_scenic_score = total_scenic_score

print(top_scenic_score)  # Part 2
