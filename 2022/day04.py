# https://adventofcode.com/2022/day/4
import common

input = common.read_file(day='04', type='final')

cleaning_pairs = input.strip().split('\n')

total_subsets = 0

for cleaning_pair in cleaning_pairs:
    cleaning_range_1, cleaning_range_2 = cleaning_pair.split(',')

    def get_cleaning_set(str_notation_range) -> set:
        beginning, end = str_notation_range.split('-')
        spaces_to_clean = range(int(beginning), int(end)+1)
        return set(spaces_to_clean)

    cleaning_set_1 = get_cleaning_set(cleaning_range_1)
    cleaning_set_2 = get_cleaning_set(cleaning_range_2)

    if cleaning_set_1.issubset(cleaning_set_2) or cleaning_set_2.issubset(cleaning_set_1):
        total_subsets += 1

print(total_subsets)  # Part 1


total_intersections = 0

for cleaning_pair in cleaning_pairs:
    cleaning_range_1, cleaning_range_2 = cleaning_pair.split(',')

    def get_cleaning_set(str_notation_range) -> set:
        beginning, end = str_notation_range.split('-')
        spaces_to_clean = range(int(beginning), int(end)+1)
        return set(spaces_to_clean)

    cleaning_set_1 = get_cleaning_set(cleaning_range_1)
    cleaning_set_2 = get_cleaning_set(cleaning_range_2)

    if cleaning_set_1.intersection(cleaning_set_2):
        total_intersections += 1

print(total_intersections)  # Part 2
