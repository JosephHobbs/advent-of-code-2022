################################################################################
# part1.py
################################################################################

import logging
from enum import Enum
from typing import Tuple

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

#

class Direction(Enum):
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'

#

class Rope():

    def __init__(self):
        self._pos_h_x = 0
        self._pos_h_y = 0
        self._pos_t_x = 0
        self._pos_t_y = 0
        self._tail_trail = []

    def _calculate_delta(self) -> Tuple:
        return (self._pos_h_x - self._pos_t_x), (self._pos_h_y - self._pos_t_y)


    @property
    def head_location(self) -> Tuple:
        return self._pos_h_x, self._pos_h_y

    def move(self, direction: Direction, steps: int):

        for _ in range(0, steps):

            if direction == Direction.DOWN:
                self._pos_h_y -= 1
            elif direction == Direction.LEFT:
                self._pos_h_x -= 1
            elif direction == Direction.RIGHT:
                self._pos_h_x += 1
            elif direction == Direction.UP:
                self._pos_h_y += 1

            self._move_tail(direction)
            self._record_tail_position()

    def _move_tail(self, direction: Direction):

        delta_x, delta_y = self._calculate_delta()
        delta_x_abs = abs(delta_x)
        delta_y_abs = abs(delta_y)

        log.debug('delta_x: %d, delta_y: %d', delta_x, delta_y)

        if direction == Direction.DOWN and delta_y_abs == 2:
            self._pos_t_y -= 1
            if delta_x_abs == 1:
                self._pos_t_x += delta_x

        elif direction == Direction.LEFT and delta_x_abs == 2:
            self._pos_t_x -= 1
            if delta_y_abs == 1:
                self._pos_t_y += delta_y

        elif direction == Direction.RIGHT and delta_x_abs == 2:
            self._pos_t_x += 1
            if delta_y_abs == 1:
                self._pos_t_y += delta_y

        elif direction == Direction.UP and delta_y_abs == 2:
            self._pos_t_y += 1
            if delta_x_abs == 1:
                self._pos_t_x += delta_x

    def _record_tail_position(self):
        position_id = f'{self._pos_t_x}:{self._pos_t_y}'
        if position_id not in self._tail_trail:
            self._tail_trail.append(position_id)

    @property
    def tail_location(self) -> Tuple:
        return self._pos_t_x, self._pos_t_y

    @property
    def tail_location_count(self) -> int:
        return len(self._tail_trail)


# Read in the contents of our INPUT.

with open('input.txt') as input_file:
    input_data = input_file.readlines()

rope = Rope()

for command_raw in input_data:
    command = command_raw.strip()

    if log.level == logging.DEBUG:
        head_x, head_y = rope.head_location
        tail_x, tail_y = rope.tail_location
        log.debug('before -> head: %d:%d | tail: %d:%d', head_x, head_y, tail_x, tail_y)

    log.debug('processing command: %s', command)

    command_parts = command.split(' ')

    rope.move(Direction(command_parts[0]), int(command_parts[1]))

    if log.level == logging.DEBUG:
        head_x, head_y = rope.head_location
        tail_x, tail_y = rope.tail_location
        log.debug('after -> head: %d:%d | tail: %d:%d', head_x, head_y, tail_x, tail_y)

for loc in rope._tail_trail:
    print(loc)
print(rope.tail_location_count)

################################################################################
# END
################################################################################
