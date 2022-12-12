# https://adventofcode.com/2022/day/6
import common

input = common.read_file(day='06', type='final')

signal = input.strip('\n')


def find_marker(signal, marker_length):
    marker_length_obo = marker_length - 1

    for count in range(len(signal)):
        if count < marker_length_obo:
            continue

        signal_window = signal[count-marker_length_obo:count+1]
        unique_characters_in_window = len(set(signal_window))

        if unique_characters_in_window == marker_length:
            print(count+1)
            break


find_marker(signal, 4)  # Part 1
find_marker(signal, 14)   # Part 2
