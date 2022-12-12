################################################################################
# part1.py  14180 too high
################################################################################

import logging
from enum import Enum
from typing import Tuple

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

#

class CPU():

    def __init__(self):
        self._cycle_count = 0
        self._register_buffer = []
        self._register_buffer.append(1)

    def exec_addx(self, x: int):
        log.debug('running addx %d', x)
        self._register_buffer.append(self._register_buffer[-1])
        self._cycle_count += 1
        log.debug('%d: register = %d', self._cycle_count, self.get_register(self._cycle_count))
        self._register_buffer.append(self._register_buffer[-1] + x)
        self._cycle_count += 1
        log.debug('%d: register = %d', self._cycle_count, self.get_register(self._cycle_count))
    
    def exec_noop(self):
        log.debug('running noop')
        self._register_buffer.append(self._register_buffer[-1])
        self._cycle_count += 1
        log.debug('%d: register = %d', self._cycle_count, self.get_register(self._cycle_count))

    def get_register(self, cycle_id: int):
        return self._register_buffer[cycle_id]

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

interesting_cycles = [20, 60, 100, 140, 180, 220]

signal_strength_sum = 0

for cycle in interesting_cycles:
    # subtract 1 from cycle when reading because we want DURING (so end of previous cycle)
    signal_strength_at_cycle = cpu.get_register(cycle - 1) * cycle
    print(f'signal strength during cycle {cycle} was {signal_strength_at_cycle}')
    signal_strength_sum += signal_strength_at_cycle

print(f'sum of interesting signal strengths is {signal_strength_sum}')

################################################################################
# END
################################################################################
