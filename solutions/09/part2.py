################################################################################
# part2.py
################################################################################

import logging
from enum import Enum
from typing import Tuple

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

#

class Direction(Enum):
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'

#

class Rope():

    def __init__(self, knot_count: int = 10):
        self.knot_count = knot_count
        self._knots = []
        for _ in range(0, knot_count):
            self._knots.append({'x': 0, 'y': 0})
        self._tail_trail = []

    def _calculate_delta(self, lead_knot_id: int, follower_knot_id: int) -> Tuple:
        delta_x = self._knots[lead_knot_id]['x'] - self._knots[follower_knot_id]['x']
        delta_y = self._knots[lead_knot_id]['y'] - self._knots[follower_knot_id]['y']
        return delta_x, delta_y

    def move(self, direction: Direction, steps: int):

        log.debug('moving %s by %d steps...', direction.name, steps)

        for _ in range(0, steps):
            if direction == Direction.DOWN:
                log.debug('moving K0 Y by -1...')
                self._knots[0]['y'] -= 1
            elif direction == Direction.LEFT:
                log.debug('moving K0 X by -1...')
                self._knots[0]['x'] -= 1
            elif direction == Direction.RIGHT:
                log.debug('moving K0 X by 1...')
                self._knots[0]['x'] += 1
            elif direction == Direction.UP:
                log.debug('moving K0 Y by 1...')
                self._knots[0]['y'] += 1
            
            log.debug('K0: %d:%d', self._knots[0]['x'], self._knots[0]['y'])

            self._move_knots()

            self._record_tail_position()

    def _move_knots(self):

        for knot_id in range(1, len(self._knots), 1):

            log.debug('K%d BEFORE: %d:%d', knot_id, self._knots[knot_id]['x'], self._knots[knot_id]['y'])

            moved_x = False
            moved_y = False
            
            delta_x, delta_y = self._calculate_delta((knot_id - 1), knot_id)
            delta_x_abs = abs(delta_x)
            delta_y_abs = abs(delta_y)

            log.debug('delta: %s:%s', delta_x, delta_y)

            if delta_x_abs == 2:
                move_by = delta_x / delta_x_abs
                log.debug('moving %d x by %d...', knot_id, move_by)
                self._knots[knot_id]['x'] += move_by
                moved_x = True

            if delta_y_abs == 2:
                move_by = delta_y / delta_y_abs
                log.debug('moving %d y by %d...', knot_id, move_by)
                self._knots[knot_id]['y'] += move_by
                moved_y = True

            if moved_y and delta_x_abs == 1:
                log.debug('moving %d x by %d...', knot_id, delta_x)
                self._knots[knot_id]['x'] += delta_x

            if moved_x and delta_y_abs == 1:
                log.debug('moving %d y by %d...', knot_id, delta_y)
                self._knots[knot_id]['y'] += delta_y

            log.debug('K%d AFTER: %d:%d', knot_id, self._knots[knot_id]['x'], self._knots[knot_id]['y'])

    def _record_tail_position(self):
        tail_knot = self._knots[self.knot_count - 1]
        position = str(int(tail_knot['x'])) + ':' + str(int(tail_knot['y']))
        if position not in self._tail_trail:
            self._tail_trail.append(position)

    @property
    def tail_location_count(self) -> int:
        return len(self._tail_trail)


# Read in the contents of our INPUT.

with open('input.txt') as input_file:
    input_data = input_file.readlines()

rope = Rope(10)

for command_raw in input_data:
    command = command_raw.strip()
    command_parts = command.split(' ')

    rope.move(Direction(command_parts[0]), int(command_parts[1]))

for loc in rope._tail_trail:
    print(loc)
print(rope.tail_location_count)

################################################################################
# END
################################################################################
