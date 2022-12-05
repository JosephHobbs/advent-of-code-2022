################################################################################
# part2.py
################################################################################

with open('input.txt') as input_file:
    input_data = input_file.readlines()

result = 0
sample_id = 0
for input_line in input_data:

    # Split each line into 2 ranges. Then split each range into start/end values.
    ranges = input_line.strip().split(',')

    range1_limits = ranges[0].split('-')
    range2_limits = ranges[1].split('-')

    range1 = range(int(range1_limits[0]), int(range1_limits[1]) + 1, 1)
    range2 = range(int(range2_limits[0]), int(range2_limits[1]) + 1, 1)

    sample_id += 1

    overlaps = False

    for value in range1:
        if value in range2:
            overlaps = True

    if not overlaps:
        for value in range2:
            if value in range1:
                overlaps = True

    if overlaps:
        print(f'ranges overlap: {range1} - {range2} - {range1_limits} - {range2_limits}')
        result += 1
    else:
        print(f'ranges do not overlap: {range1} - {range2} - {range1_limits} - {range2_limits}')

print(f'Result: {result}')

################################################################################
# END
################################################################################
