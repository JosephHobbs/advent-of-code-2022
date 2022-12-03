################################################################################
# part1.py
################################################################################

with open('input.txt') as input_file:
    input_data = input_file.readlines()

total_priority = 0

for input_line in input_data:

    # Clean up the contents and split it into two compartments...

    contents = input_line.strip()
    half_items = int(len(contents) / 2)
    c1 = contents[:half_items]
    c2 = contents[half_items:]

    print(f'Sack: {contents}, C1: {c1}, C2: {c2}')

    for item in c1:
        if item in c2:
            
            item_priority = ord(item)

            print(f'item {item} [{item_priority}]found in both compartments...')

            if item_priority >= 97:
                item_priority -= 96
            else:
                item_priority -= 38

            print(f'  calculated item priority as {item_priority}')

            total_priority += item_priority

            break

print(f'Total: {total_priority}')

################################################################################
# END
################################################################################
