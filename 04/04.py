
import re

def validate_post(field, value):
    def validate_byr(value):
        return 1920 <= int(value) <= 2002

    def validate_iyr(value):
        return 2010 <= int(value) <= 2020

    def validate_eyr(value):
        return 2020 <= int(value) <= 2030

    def validate_hgt(value):
        if value[-2:] == 'cm':
            return 150 <= int(value[:-2]) <= 193
        
        elif value[-2:] == 'in':
            return 59 <= int(value[:-2]) <= 76

        else:
            return False

    def validate_hcl(value):
        return bool(re.match(r'^#[0-9|a-f]{6}$', value))

    def validate_ecl(value):
        return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

    def validate_pid(value):
        return bool(re.match(r'^[0-9]{9}$', value))

    return {
        'byr': validate_byr,
        'iyr': validate_iyr,
        'eyr': validate_eyr,
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': validate_pid
    }.get(field, lambda v: False)(value)


with open("input", "r") as input_file:
    input_data = input_file.read()

passports = input_data.replace('\n', ' ').split("  ")

n_valid_task1 = 0
n_valid_task2 = 0

required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

i = 0
for pp in passports:
    # Task 1 test
    is_valid_task1 = True
    for field in required_fields:

        if field not in pp:
            is_valid_task1 = False
            break

    n_valid_task1 += is_valid_task1

    # Task 2 test
    if not is_valid_task1:
        continue
    
    n_valid_fields = 0
    for post in pp.split(' '):
        field, value, *_ = post.split(':')
        
        n_valid_fields += validate_post(field, value)
    
    n_valid_task2 += (n_valid_fields == 7)


print(n_valid_task1)
print(n_valid_task2)