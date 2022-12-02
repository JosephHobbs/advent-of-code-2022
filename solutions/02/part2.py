################################################################################
# part1.py
################################################################################

#
# ROCK = 1
# PAPER = 2
# SCISSORS = 3
# LOSE = 0
# DRAW = 3
# WIN = 6
#

scenarios = {
    'A X': 3,   # OP:ROCK     ME:SCISSOR OUTCOME:LOSE
    'A Y': 4,   # OP:ROCK     ME:ROCK    OUTCOME:DRAW
    'A Z': 8,   # OP:ROCK     ME:PAPER   OUTCOME:WIN
    'B X': 1,   # OP:PAPER    ME:ROCK    OUTCOME:LOSE
    'B Y': 5,   # OP:PAPER    ME:PAPER   OUTCOME:DRAW
    'B Z': 9,   # OP:PAPER    ME:SCISSOR OUTCOME:WIN
    'C X': 2,   # OP:SCISSORS ME:PAPER   OUTCOME:LOSE
    'C Y': 6,   # OP:SCISSORS ME:SCISSOR OUTCOME:DRAW
    'C Z': 7    # OP:SCISSORS ME:ROCK    OUTCOME:WIN
}

with open('input.txt') as input_file:
    input_data = input_file.readlines()

score = 0

for input_line in input_data:

    score += scenarios[input_line.strip()]

print(score)

################################################################################
# END
################################################################################
