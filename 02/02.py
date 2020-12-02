import re

with open("input", "r") as input_file:
    test_strings = list(input_file)

re_test = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

n_valid_task1 = 0
n_valid_task2 = 0
for s in test_strings:
    match = re_test.search(s)

    m = int(match.group(1))
    n = int(match.group(2))

    ch = match.group(3)
    pw = match.group(4)

    if m <= pw.count(ch) <= n:
        n_valid_task1 += 1

    if (pw[m - 1] == ch) ^ (pw[n - 1] == ch):
        n_valid_task2 += 1 

print(n_valid_task1)
print(n_valid_task2)