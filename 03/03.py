def count_collisions(slope_map, x_step, y_step):
    slope_width = len(slope_map[0])

    n_trees_hit = 0
    x_pos = 0
    for y_pos in range(0, len(slope_map), y_step):
        n_trees_hit += (slope_map[y_pos][x_pos] == '#')

        x_pos = (x_pos + x_step) % (slope_width - 1)

    return n_trees_hit


with open("input", "r") as input_file:
    tree_strings = list(input_file)

movement_patterns = [(1,1), (3,1), (5,1), (7,1), (1,2)]

multiplied_collissions = 1
for mp in movement_patterns:
    multiplied_collissions *= count_collisions(tree_strings, *mp)

print(count_collisions(tree_strings, 3, 1))
print(multiplied_collissions)