################################################################################
# part1.py
################################################################################

with open('input.txt') as input_file:
    input_data = input_file.readlines()


stacks = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}

stack_lines = []

reading_stack = True
calc_columns = False
apply_deltas = False


for input_line_raw in input_data:
    input_line = input_line_raw.strip()

    # Skip the empty line...

    if input_line == '':
        print('skipping empty line')
        continue

    # Process in our stack header...

    if reading_stack:

        if input_line.startswith('1   2'):
            print('skipping stack count label row')
            reading_stack = False
            calc_columns = True
            continue
        else:
            print('adding stack row to stack_lines')
            stack_lines.append(input_line)
            continue

    # Calculate our current stack state...

    if calc_columns:

        target_row = len(stack_lines) - 1

        while target_row >= 0:

            row_as_chars = [*stack_lines[target_row]]

            current_col = 1
            for stack_col_id in range(1, 36, 4):
                if(len(row_as_chars) >= stack_col_id):
                    if(row_as_chars[stack_col_id] != ' '):
                        stacks[current_col].append(row_as_chars[stack_col_id])
                
                current_col += 1

            target_row -= 1
            

        calc_columns = False
        apply_deltas = True

    if apply_deltas:

        delta_fields = input_line.split()
        move_qty = int(delta_fields[1])
        move_from = int(delta_fields[3])
        move_to = int(delta_fields[5])

        stack_o_crates = []
        for unit in range(1, move_qty + 1):
            stack_o_crates.append(stacks[move_from].pop(-1))

        stacks[move_to].extend(stack_o_crates)

result = ''

for col_id in stacks:
    stack = stacks[col_id]
    result += stack[len(stack) - 1]

print(result)

################################################################################
# END
################################################################################
