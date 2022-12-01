################################################################################
# part1.py
################################################################################

data = []

with open('input.txt') as input_file:
    input_data = input_file.readlines()

total_calories = 0
for input_line in input_data:

    value = input_line.strip()

    if value != '':
        total_calories += int(value)
    else:
        data.append(total_calories)
        total_calories = 0

largest_payload = 0

for elf_payload in data:
    if elf_payload > largest_payload:
        largest_payload = elf_payload

print(largest_payload)

################################################################################
# END
################################################################################
