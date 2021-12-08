# Part 1
# Determine the horizontal position that the crabs can align to using the least fuel possible.
# How much fuel must they spend to align to that position?

from typing import List

test_input = [16,1,2,0,4,2,7,1,2,14]


def required_fuel(n: int, positions: List[int]) -> int:
    return sum([abs(x - n) for x in positions])

assert required_fuel(2, test_input) == 37

# sum of numbers 1 -> n
def sum_n(n: int):
    return (n * (n + 1)) / 2

def required_fuel_2(n: int, positions: List[int]) -> int:
    return sum([sum_n(abs(x - n)) for x in positions])

assert required_fuel_2(5, test_input) == 168

# I know this is bad but I went to a concert tonight and its late and I'm tired
def gross_brute_force(input: List[int]):
    ideal_pos = None
    min_fuel = float('inf')
    for i in range(min(input), max(input)):
        fuel = required_fuel_2(i, input)
        if fuel < min_fuel:
            min_fuel = fuel
            ideal_pos = i
    return (ideal_pos, min_fuel)

assert gross_brute_force(test_input) == (5, 168)

with open('data/day07.txt', 'r') as f:
    inputs = [int(x) for x in f.read().strip().split(',')]
    print(gross_brute_force(inputs))
