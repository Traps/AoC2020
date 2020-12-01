def find_combination_sum(tail, n_values, target_sum):
    while tail:
        head, *tail = tail

        if head > target_sum:
            continue

        if (n_values == 1) and (head == target_sum):
            return head
        
        elif n_values > 1:
            v = find_combination_sum(tail, n_values - 1, target_sum - head)
            if v:
                return head * v

    return None

solution = 2020

input_file = open("input", "r")

input_text = input_file.read()

input_file.close()

input_values = [int(s) for s in input_text.splitlines()]

print(find_combination_sum(input_values, 2, 2020))
print(find_combination_sum(input_values, 3, 2020))