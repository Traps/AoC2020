from collections import defaultdict

def check_for_gold(bag_rules, colour):
    if not bag_rules[colour]:
        return False

    if 'shiny gold' in bag_rules[colour]:
        return True

    for c in bag_rules[colour]:
        if check_for_gold(bag_rules, c):
            return True

    return False

def count_bags_in_bag(bag_rules, colour):
    if not bag_rules[colour]:
        return 0
    
    n_in_bag = 0
    for c in bag_rules[colour]:
        n_in_bag += bag_rules[colour][c] + bag_rules[colour][c] * count_bags_in_bag(bag_rules, c)

    return n_in_bag


with open("input", "r") as input_file:
    rule_lines = list(input_file)

bag_rules = defaultdict(lambda: {})
for rule_line in rule_lines:
    outer_bag, inner_bag = rule_line.replace(' bags','').replace(' bag', '').replace('.','').split(' contain ')

    bag_rules[outer_bag] = defaultdict(lambda: 0)
    for b in inner_bag.split(', '):
        if "no other" not in b:
            n, *c = b.split(' ', 1)
        
            bag_rules[outer_bag][c[0].strip('\n')] = int(n)

n_holds_gold = 0
for c in bag_rules:
    n_holds_gold += check_for_gold(bag_rules, c)

print(n_holds_gold)
print(count_bags_in_bag(bag_rules, 'shiny gold'))