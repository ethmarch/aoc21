# Part 1
'''
A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0
is included as a valid timer value). The new lanternfish starts with an internal
timer of 8 and does not start counting down until the next day.

Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?
'''
from typing import List

test_input = [3,4,3,1,2]

def descendents(state: int, timer: int, lookup: dict) -> int:
    if timer == 0:
        return 1
    elif (state, timer) in lookup:
        return lookup.get((state, timer))
    elif state == 0:
        n = descendents(6, timer - 1, lookup) + descendents(8, timer - 1, lookup)
        lookup[(state, timer)] = n
        return n
    else:
        n = descendents(state - 1, timer - 1, lookup)
        lookup[(state, timer)] = n
        return n
def count_lanternfish(inital_states: List[int], time: int) -> int:
    lookup = {}
    return sum([descendents(x, time, lookup) for x in inital_states])

assert count_lanternfish(test_input, 18) == 26
assert count_lanternfish(test_input, 80) == 5934

with open('data/day06.txt', 'r') as f:
    states = [int(x) for x in f.read().strip().split(',')]
    print(count_lanternfish(states, 256))

# Part 2
# How many lanternfish would there be after 256 days?

# Added memoization to descendents calc