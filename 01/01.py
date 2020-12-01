from itertools import combinations
import numpy as np

solution = 2020

input_file = open("input", "r")

input_text = input_file.read()

input_file.close()

input_values = [int(s) for s in input_text.splitlines()]

# Part 1
for c in combinations(input_values, 2):
    if sum(c) == solution:
        print(np.prod(c))
        break

# Part 2
for c in combinations(input_values, 3):
    if sum(c) == solution:
        print(np.prod(c))
        break