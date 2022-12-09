################################################################################
# part2.py
################################################################################

import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# Read in the contents of our INPUT.

with open('input.txt') as input_file:
    input_data = input_file.readlines()

# Use the provided input data to build our tree grid.

trees = []
for input_line_raw in input_data:

    tree_row = []
    for tree in input_line_raw.strip():
        tree_row.append(int(tree))

    trees.append(tree_row)

# Process the grid for each tree to see if it is visible or not. Since the 
# outer trees can't be hidden, use a range that ignores the first/last col/row.

scenic_score = 0

for ct_row in range(0, len(trees)):

    for ct_column in range(0, len(trees[ct_row])):

        current_tree = trees[ct_row][ct_column]

        vN = 0
        vS = 0
        vE = 0
        vW = 0
        
        log.debug('processing tree %d:%d with height %d', ct_row, ct_column, current_tree)

        if ct_row == 0:
            vN += 1

        for ot_row in range(ct_row - 1, -1, -1):
            vN += 1
            if trees[ot_row][ct_column] >= current_tree:
                break

        if ct_row == len(trees):
            vS += 1

        for ot_row in range(ct_row + 1, len(trees), 1):
            vS += 1
            if trees[ot_row][ct_column] >= current_tree:
                break

        if ct_column == len(trees[ct_row]):
            vE += 1

        for ot_column in range(ct_column + 1, len(trees[ct_row]), 1):
            vE += 1
            if trees[ct_row][ot_column] >= current_tree:
                break

        if ct_column == 0:
            vW += 1

        for ot_column in range(ct_column - 1, -1, -1):
            vW += 1
            if trees[ct_row][ot_column] >= current_tree:
                break

        current_scenic_score = 1
        if vN > 0:
            current_scenic_score *= vN
        if vS > 0:
            current_scenic_score *= vS
        if vE > 0:
            current_scenic_score *= vE
        if vW > 0:
            current_scenic_score *= vW

        if current_scenic_score > scenic_score:
            scenic_score = current_scenic_score

print(scenic_score)

################################################################################
# END
################################################################################

