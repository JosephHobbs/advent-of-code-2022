################################################################################
# part1.py
################################################################################

import logging
from typing import Tuple

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

#

class Rope():

    def __init__(self):
        self._pos_H_X = 0
        self._pos_H_Y = 0
        self._pos_T_X = 0
        self._pos_T_Y = 0
        self.tail_trail = {}

    @property
    def head_location(self) -> Tuple:
        return self._pos_H_X, self._pos_H_Y

    def move_down(self, steps: int):
        log.debug('moving down %d', steps)
        for step in range(0, steps, 1):
            self._pos_H_Y -= 1

    def move_left(self, steps: int):
        log.debug('moving left %d', steps)
        for step in range(0, steps, 1):
            self._pos_H_X -= 1

    def move_right(self, steps: int):
        log.debug('moving right %d', steps)
        for step in range(0, steps, 1):
            self._pos_H_X += 1

    def move_up(self, steps: int):
        log.debug('moving up %d', steps)
        for step in range(0, steps, 1):
            self._pos_H_Y += 1

    @property
    def tail_location(self) -> Tuple:
        return self._pos_T_X, self._pos_T_Y



# Read in the contents of our INPUT.

with open('input.txt') as input_file:
    input_data = input_file.readlines()

rope = Rope()

for command_raw in input_data:
    command = command_raw.strip()

    log.debug('processing command: %s', command)

    command_parts = command.split(' ')

    if command_parts[0] == 'D':
        rope.move_down(int(command_parts[1]))
    elif command_parts[0] == 'L':
        rope.move_left(int(command_parts[1]))
    elif command_parts[0] == 'R':
        rope.move_right(int(command_parts[1]))
    elif command_parts[0] == 'U':
        rope.move_up(int(command_parts[1]))

print(rope.head_location)

################################################################################
# END 1855 too high
################################################################################
