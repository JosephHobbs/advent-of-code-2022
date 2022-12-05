################################################################################
# part1.py
################################################################################

with open('input.txt') as input_file:
    input_data = input_file.readlines()

result = 0
sample_id = 0
for input_line in input_data:

    # Split each line into 2 ranges. Then split each range into start/end values.
    ranges = input_line.strip().split(',')
    range1 = ranges[0].split('-')
    range2 = ranges[1].split('-')

    sample_id += 1

    if int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1]):
        print(f'{sample_id} - range1 in range2 - {range1[0]} - {range1[1]} ... {range2[0]} - {range2[1]}')
        result += 1
        continue

    elif int(range2[0]) >= int(range1[0]) and int(range2[1]) <= int(range1[1]):
        print(f'{sample_id} - range2 in range1 - {range1[0]} - {range1[1]} ... {range2[0]} - {range2[1]}')
        result += 1

    else:
        print(f'{sample_id} - NOPE             - {range1[0]} - {range1[1]} ... {range2[0]} - {range2[1]}')
        

print(f'Result: {result}')

################################################################################
# END
################################################################################
