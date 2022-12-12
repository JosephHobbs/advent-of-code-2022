################################################################################
# part2.py
################################################################################

import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

#

class CPU():

    def __init__(self):
        self.cycle_count = 0
        self._register_buffer = []
        self._register_buffer.append(1)

    def exec_addx(self, x: int):
        log.debug('running addx %d', x)
        self._register_buffer.append(self._register_buffer[-1])
        self.cycle_count += 1
        log.debug('%d: register = %d', self.cycle_count, self.get_register(self.cycle_count))
        self._register_buffer.append(self._register_buffer[-1] + x)
        self.cycle_count += 1
        log.debug('%d: register = %d', self.cycle_count, self.get_register(self.cycle_count))
    
    def exec_noop(self):
        log.debug('running noop')
        self._register_buffer.append(self._register_buffer[-1])
        self.cycle_count += 1
        log.debug('%d: register = %d', self.cycle_count, self.get_register(self.cycle_count))

    def get_register(self, cycle_id: int):
        return self._register_buffer[cycle_id - 1]

class Screen():

    def __init__(self, columns: int = 40, rows: int = 6):
        self._columns = columns
        self._rows = rows
        self._buffer = []
        for _ in range(0, rows):
            initlal_pixel_row = []
            for _ in range(0, columns):
                initlal_pixel_row.append('.')
            self._buffer.append(initlal_pixel_row)

    def get_screen(self):
        result = ''
        for row in self._buffer:
            for column_id in range(0, self._columns):
                result += row[column_id]
            result += '\n'
        return result

    def light_pixel(self, column: int, row: int):
        self._buffer[row][column] = '#'

# Read in the contents of our INPUT.

with open('input.txt') as input_file:
    input_data = input_file.readlines()

#

cpu = CPU()

for input_line_raw in input_data:
    input_line = input_line_raw.strip()

    if input_line == 'noop':
        cpu.exec_noop()
    
    elif input_line.startswith('addx '):
        cpu.exec_addx(int(input_line.split(' ', 2)[1]))

#

SCREEN_COLUMNS = 40
SCREEN_ROWS = 6

screen = Screen(SCREEN_COLUMNS, SCREEN_ROWS)

for cycle in range(1, cpu.cycle_count):
    row, column = divmod(cycle - 1, SCREEN_COLUMNS)
    log.debug('cycle %d targets %d:%d', cycle, row, column)
    sprite_location = cpu.get_register(cycle)
    log.debug('sprite location: %d', sprite_location)

    if sprite_location >= (column - 1) and sprite_location <= (column + 1):
        screen.light_pixel(column, row)

print(screen.get_screen())

################################################################################
# END
################################################################################
