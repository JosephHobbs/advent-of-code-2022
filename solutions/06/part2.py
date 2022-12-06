################################################################################
# part2.py
################################################################################

with open('input.txt') as input_file:
    input_data = input_file.read().strip()

buffer = []
letter_id = 0

for letter in input_data:

    # keep track of the current character id

    letter_id += 1

    # if our buffer is full, drop the first char.

    if len(buffer) == 14:
        buffer.pop(0)

    # add the new char to the end of our buffer.

    buffer.append(letter)

    # if we have 4 unique, we have a start of packet.

    if letter_id > 13 and len(buffer) == len(set(buffer)):
        print(letter_id)

################################################################################
# END
################################################################################
