# https://adventofcode.com/2022/day/3
import common

input = common.read_file(day='03', type='final')

rucksacks = input.strip().split('\n')

total_priority = 0

for rucksack in rucksacks:
    half_rucksack_size = len(rucksack)//2
    compartment_1, compartment_2 = rucksack[:half_rucksack_size], rucksack[half_rucksack_size:]

    intersection = set(compartment_1).intersection(compartment_2)
    shared_item = list(intersection)[0]
    if shared_item.islower():
        priority = ord(shared_item) - 96
    else:
        priority = ord(shared_item) - 38

    total_priority += priority

print(total_priority)  # Part 1


total_priority = 0

for i in range(0, len(rucksacks), 3):
    elf_1_rucksack = rucksacks[i]
    elf_2_rucksack = rucksacks[i+1]
    elf_3_rucksack = rucksacks[i+2]

    intersection = set(elf_1_rucksack).intersection(elf_2_rucksack).intersection(elf_3_rucksack)
    shared_item = list(intersection)[0]
    if shared_item.islower():
        priority = ord(shared_item) - 96
    else:
        priority = ord(shared_item) - 38

    total_priority += priority

print(total_priority)  # Part 2
