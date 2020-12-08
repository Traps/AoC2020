def flip_operation(op):
    return 'jmp' if op == 'nop' else 'nop'

def run_program(instructions, i_op = 0, accumulator = 0, instruction_executed = None):
    if i_op < 0 or i_op >= len(instructions):
        return False

    if not instruction_executed:
        instruction_executed = [False for _ in range(len(instructions))]

    while not instruction_executed[i_op]:
        instruction_executed[i_op] = True

        if instructions[i_op]['operation'] == 'acc':
            accumulator += instructions[i_op]['value']

        elif instructions[i_op]['operation'] == 'jmp':
            i_op += instructions[i_op]['value'] - 1

        elif instructions[i_op]['operation'] == 'nop':
            pass

        i_op += 1

        if i_op < 0:
            return 0

        elif i_op >= len(instructions):
            return (i_op, accumulator)

    return (i_op, accumulator)

def run_program_part_two(instructions):
    n_instructions = len(instructions)

    instruction_executed = [False for _ in range(n_instructions)]

    i_op = 0
    accumulator = 0

    while 0 <= i_op <= n_instructions and not instruction_executed[i_op]:
        instruction_executed[i_op] = True
        
        if instructions[i_op]['operation'] == 'acc':
            accumulator += instructions[i_op]['value']

        elif instructions[i_op]['operation'] == 'jmp':
            (i, acc) = run_program(instructions, i_op + 1, accumulator, instruction_executed[:])
            if i == n_instructions:
                return (i, acc)

            i_op += instructions[i_op]['value'] - 1

        elif instructions[i_op]['operation'] == 'nop':
            (i, acc) = run_program(instructions, i_op + instructions[i_op]['value'], accumulator, instruction_executed[:])
            if i == n_instructions:
                return (i, acc)

        i_op += 1


with open("input", "r") as input_file:
    instruction_lines = [line.strip('\n') for line in list(input_file)]

instructions = []
for instruction in instruction_lines:
    op, vs = instruction.split(' ')

    v = int(vs[1:]) if vs[0] == '+' else -int(vs[1:])

    instructions.append({'operation':op, 'value':v})




print(run_program(instructions))
print(run_program_part_two(instructions))