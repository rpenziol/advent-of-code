# https://adventofcode.com/2022/day/1
import common

input = common.read_file(day='01', type='final')

elves_calories = input.strip().split('\n\n')

each_elfs_total_calories = []

for meals_calories in elves_calories:
    amount = [int(x) for x in meals_calories.split('\n')]
    each_elfs_total_calories.append(sum(amount))

print(max(each_elfs_total_calories))  # Part 1

each_elfs_total_calories.sort()
print(sum(each_elfs_total_calories[-3:])) # Part 2
