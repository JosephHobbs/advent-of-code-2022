################################################################################
# part1.py
################################################################################

def get_group_priority(sacks: list) -> int:

    for item in sacks[0]:
        if item in sacks[1] and item in sacks[2]:

            item_priority = ord(item)

            if item_priority >= 97:
                item_priority -= 96
            else:
                item_priority -= 38
            
            break

    return item_priority

#
# 
#

with open('input.txt') as input_file:
    input_data = input_file.readlines()

total_priority = 0

group_sacks = []

for input_line in input_data:

    if len(group_sacks) < 3:
        group_sacks.append(input_line.strip())

    else:

        total_priority += get_group_priority(group_sacks)

        group_sacks.clear()
        group_sacks.append(input_line.strip())

total_priority += get_group_priority(group_sacks)

print(f'Total: {total_priority}')

################################################################################
# END
################################################################################
