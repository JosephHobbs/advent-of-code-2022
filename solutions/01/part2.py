################################################################################
# part2.py
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

data.sort(reverse=True)

print(data[0] + data[1] + data[2])

################################################################################
# END
################################################################################
