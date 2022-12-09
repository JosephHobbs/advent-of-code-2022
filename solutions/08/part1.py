################################################################################
# part1.py
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

visible_trees = 99 + 99 + 97 + 97

for ct_row in range(1, len(trees) - 1):

    for ct_column in range(1, len(trees[ct_row]) - 1):

        is_hidden_N = False
        is_hidden_S = False
        is_hidden_E = False
        is_hidden_W = False
        current_tree = trees[ct_row][ct_column]

        log.debug('processing tree %d:%d with height %d', ct_row, ct_column, current_tree)

        for ot_row in range(0, len(trees)):

            log.debug('checking visibility against row %d', ot_row)

            if ot_row == ct_row:
                for ot_column in range(0, len(trees[ot_row])):
                    log.debug('comparing against tree at %d:%d', ot_row, ot_column)
                    if ot_column < ct_column:
                        log.debug('is %d taller than %d?', trees[ot_row][ot_column], current_tree)
                        if trees[ot_row][ot_column] >= current_tree:
                            log.debug('yes, tree is not visible')
                            is_hidden_W = True
                    elif ot_column > ct_column:
                        log.debug('is %d taller than %d?', trees[ot_row][ot_column], current_tree)
                        if trees[ot_row][ot_column] >= current_tree:
                            log.debug('yes, tree is not visible')
                            is_hidden_E = True
                    else:
                        log.debug('skipping current tree')

            else:

                log.debug('comparing against tree at %d:%d', ot_row, ct_column)

                if ot_row < ct_row:
                    log.debug('is %d taller than %d?', trees[ot_row][ct_column], current_tree)
                    if trees[ot_row][ct_column] >= current_tree:
                        log.debug('yes, tree is not visible')
                        is_hidden_N = True
                elif ot_row > ct_row:
                    log.debug('is %d taller than %d?', trees[ot_row][ct_column], current_tree)
                    if trees[ot_row][ct_column] >= current_tree:
                        log.debug('yes, tree is not visible')
                        is_hidden_S = True
                else:
                    log.debug('skipping current tree')

        if not (is_hidden_N and is_hidden_S and is_hidden_E and is_hidden_W):
            visible_trees += 1

print(visible_trees)

################################################################################
# END 1855 too high
################################################################################
