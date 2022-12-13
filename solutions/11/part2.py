################################################################################
# part1.py
################################################################################

import logging
import math
from typing import List, Tuple

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

class Monkey():

    def __init__(
        self, monkey_id: int, items: List[int], worry_operation: str,
        decision_divisor: str, target_if_true: int, target_if_false: int):

        self.id = monkey_id
        self._items = items
        self._worry_op = worry_operation
        self._decision_divisor = decision_divisor
        self._target_if_true = target_if_true
        self._target_if_false = target_if_false
        self.items_inspected = 0

    def _calculate_worry_level(self, worry_level: int) -> int:

        operation, modifier = tuple(self._worry_op.split(' '))

        if modifier == 'old':
            modifier = worry_level

        if operation == '+':
            elevated_worry_level = worry_level + int(modifier)
        else:
            elevated_worry_level =  worry_level * int(modifier)

        return elevated_worry_level

    def _choose_target(self, worry_level: int) -> int:

        if (worry_level % self._decision_divisor == 0):
            return self._target_if_true
        else:
            return self._target_if_false

    def catch_item(self, item: int):
        log.debug('%d: caught item %d', self.id, item)
        self._items.append(item)

    def has_items(self) -> bool:
        return (len(self._items) > 0)

    def inspect_and_throw(self, least_common_multiple: int) -> Tuple:

        self.items_inspected += 1

        current_item = self._items.pop(0)

        log.debug('%d: processing item %d', self.id, current_item)

        updated_item = self._calculate_worry_level(current_item)

        log.debug('%d: updated worry level is %d', self.id, updated_item)

        updated_item %= least_common_multiple

        log.debug('%d: modulod worry level is %d', self.id, updated_item)

        target_monkey = self._choose_target(updated_item)

        log.debug('%d: target monkey is %d', self.id, target_monkey)

        return updated_item, target_monkey

monkeys = []

# Monkey 0:
#   Starting items: 61
#   Operation: new = old * 11
#   Test: divisible by 5
#     If true: throw to monkey 7
#     If false: throw to monkey 4

monkeys.append(
    Monkey(
        monkey_id=0,
        items=[61],
        worry_operation='* 11',
        decision_divisor=5,
        target_if_true=7,
        target_if_false=4
    ))

# Monkey 1:
#   Starting items: 76, 92, 53, 93, 79, 86, 81
#   Operation: new = old + 4
#   Test: divisible by 2
#     If true: throw to monkey 2
#     If false: throw to monkey 6

monkeys.append(
    Monkey(
        monkey_id=1,
        items=[76, 92, 53, 93, 79, 86, 81],
        worry_operation='+ 4',
        decision_divisor=2,
        target_if_true=2,
        target_if_false=6
    ))

# Monkey 2:
#   Starting items: 91, 99
#   Operation: new = old * 19
#   Test: divisible by 13
#     If true: throw to monkey 5
#     If false: throw to monkey 0

monkeys.append(
    Monkey(
        monkey_id=2,
        items=[91, 99],
        worry_operation='* 19',
        decision_divisor=13,
        target_if_true=5,
        target_if_false=0
    ))

# Monkey 3:
#   Starting items: 58, 67, 66
#   Operation: new = old * old
#   Test: divisible by 7
#     If true: throw to monkey 6
#     If false: throw to monkey 1

monkeys.append(
    Monkey(
        monkey_id=3,
        items=[58, 67, 66],
        worry_operation='* old',
        decision_divisor=7,
        target_if_true=6,
        target_if_false=1
    ))

# Monkey 4:
#   Starting items: 94, 54, 62, 73
#   Operation: new = old + 1
#   Test: divisible by 19
#     If true: throw to monkey 3
#     If false: throw to monkey 7

monkeys.append(
    Monkey(
        monkey_id=4,
        items=[94, 54, 62, 73],
        worry_operation='+ 1',
        decision_divisor=19,
        target_if_true=3,
        target_if_false=7
    ))

# Monkey 5:
#   Starting items: 59, 95, 51, 58, 58
#   Operation: new = old + 3
#   Test: divisible by 11
#     If true: throw to monkey 0
#     If false: throw to monkey 4

monkeys.append(
    Monkey(
        monkey_id=5,
        items=[59, 95, 51, 58, 58],
        worry_operation='+ 3',
        decision_divisor=11,
        target_if_true=0,
        target_if_false=4
    ))

# Monkey 6:
#   Starting items: 87, 69, 92, 56, 91, 93, 88, 73
#   Operation: new = old + 8
#   Test: divisible by 3
#     If true: throw to monkey 5
#     If false: throw to monkey 2

monkeys.append(
    Monkey(
        monkey_id=6,
        items=[87, 69, 92, 56, 91, 93, 88, 73],
        worry_operation='+ 8',
        decision_divisor=3,
        target_if_true=5,
        target_if_false=2
    ))

# Monkey 7:
#   Starting items: 71, 57, 86, 67, 96, 95
#   Operation: new = old + 7
#   Test: divisible by 17
#     If true: throw to monkey 3
#     If false: throw to monkey 1

monkeys.append(
    Monkey(
        monkey_id=7,
        items=[71, 57, 86, 67, 96, 95],
        worry_operation='+ 7',
        decision_divisor=17,
        target_if_true=3,
        target_if_false=1
    ))

#
#
#

least_common_multiple = 1
for monkey in monkeys:
    for item in monkey._items:
        least_common_multiple = lcm(least_common_multiple, item)

for round in range(0, 10000):
    print(f'ROUND {round}')
    for monkey in monkeys:
        while monkey.has_items():
            item, target = monkey.inspect_and_throw(least_common_multiple)
            print(f'sending {item} to monkey {target}')
            monkeys[target].catch_item(item)

inspection_counts = []
for monkey in monkeys:
    inspection_counts.append(monkey.items_inspected)

inspection_counts.sort(reverse=True)

print(inspection_counts[0] * inspection_counts[1])

################################################################################
# END
################################################################################
