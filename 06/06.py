with open("input", "r") as input_file:
    input_data = input_file.read()

group_declarations = input_data.replace('\n', ' ').split("  ")

any_sum = 0
common_sum = 0
for gd in group_declarations:
    any_sum += len(set(gd.replace(' ','')))

    common_set = None
    for d in gd.split(' '):
        common_set = common_set.intersection(set(d)) if common_set != None else set(d)

    common_sum += len(common_set)

print(any_sum)
print(common_sum)