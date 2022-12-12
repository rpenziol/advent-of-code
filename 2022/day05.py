# https://adventofcode.com/2022/day/5
import common
import re

input = common.read_file(day='05', type='final')

setup, instructions = input.split('\n\n')

cargo_rows = setup.split('\n')[:-1]
column_labels = setup.split('\n')[-1:][0].split()


def create_cargo_stacks(column_labels, cargo_rows):
    cargo_stacks = {}
    for column_label in column_labels:
        cargo_stacks[column_label] = []

    for cargo_row in reversed(cargo_rows):
        cargo_row += ' '  # Parsing hack to make regex work
        cargo_columns = re.findall('....', cargo_row)

        for column_number, cargo in enumerate(cargo_columns):
            column_label = str(column_number + 1)
            cargo = cargo.strip(' []')
            if cargo:
                cargo_stacks[column_label].append(cargo)

    return cargo_stacks


def print_result(column_labels, cargo_stacks):
    result = ''
    for column_label in column_labels:
        result += cargo_stacks[column_label][-1]

    print(result)


cargo_stacks = create_cargo_stacks(column_labels, cargo_rows)
for step in instructions.split('\n')[:-1]:
    amount, from_column, to_column = re.search(r"move (\d+) from (\d+) to (\d+)", step).groups()

    for i in range(int(amount)):
        current_cargo = cargo_stacks[from_column].pop()
        cargo_stacks[to_column].append(current_cargo)

result = ''
for column_label in column_labels:
    result += cargo_stacks[column_label][-1]

print_result(column_labels, cargo_stacks)  # Part 1


cargo_stacks = create_cargo_stacks(column_labels, cargo_rows)

for step in instructions.split('\n')[:-1]:
    amount, from_column, to_column = re.search(r"move (\d+) from (\d+) to (\d+)", step).groups()

    current_cargo = cargo_stacks[from_column][-int(amount):]
    del cargo_stacks[from_column][-int(amount):]
    cargo_stacks[to_column].extend(current_cargo)

print_result(column_labels, cargo_stacks)  # Part 2
