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
    'A X': 4,   # OP:ROCK     ME:ROCK     OUTCOME:DRAW
    'A Y': 8,   # OP:ROCK     ME:PAPER    OUTCOME:WIN
    'A Z': 3,   # OP:ROCK     ME:SCISSORS OUTCOME:LOSE
    'B X': 1,   # OP:PAPER    ME:ROCK     OUTCOME:LOSE
    'B Y': 5,   # OP:PAPER    ME:PAPER    OUTCOME:DRAW
    'B Z': 9,   # OP:PAPER    ME:SCISSORS OUTCOME:WIN
    'C X': 7,   # OP:SCISSORS ME:ROCK     OUTCOME:WIN
    'C Y': 2,   # OP:SCISSORS ME:PAPER    OUTCOME:LOSE
    'C Z': 6    # OP:SCISSORS ME:SCISSORS OUTCOME:DRAW
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
