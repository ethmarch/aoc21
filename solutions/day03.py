# Part 1

# Each bit in the gamma rate can be determined by finding the most 
# common bit in the corresponding position of all numbers in the diagnostic report.

# The epsilon rate is calculated in a similar way; rather than use the most common bit,
# the least common bit from each position is used.

from typing import List
import math


raw_test = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''

def parse_input(input: str) -> List[List[int]]:
    lines = input.splitlines()
    return [[int(x) for x in line] for line in lines]


def gamma_rate(report: List[List[int]]) -> str:
    majority = math.ceil(len(report) / 2)
    pos_sums = [sum(list(x)) for x in zip(*report)]
    return ''.join([str(int(x >= majority)) for x in pos_sums])
   

def epsilon_rate(report: List[List[int]]) -> str:
    majority = math.ceil(len(report) / 2)
    pos_sums = [sum(list(x)) for x in zip(*report)]
    return ''.join([str(int(majority > x)) for x in pos_sums])

test_report = parse_input(raw_test)
assert int(gamma_rate(test_report), base=2) == 22
assert int(epsilon_rate(test_report), base=2) == 9

with open('data/day03.txt', 'r') as f:
    raw = f.read() 
report = parse_input(raw)
print(int(epsilon_rate(report), base=2) * int(gamma_rate(report), base=2))

# Part 2

def o2_gen_rating(report: List[List[int]]) -> int:
    result = report
    i = 0
    while len(result) > 1:
        most_common = gamma_rate(result)
        result = [x for x in result if x[i] == int(most_common[i])]
        i += 1
    return int(''.join([str(x) for x in result[0]]), base=2)

assert o2_gen_rating(test_report) == 23

def co2_scrub_rating(report: List[List[int]]) -> int:
    result = report
    i = 0
    while len(result) > 1:
        least_common = epsilon_rate(result)
        result = [x for x in result if x[i] == int(least_common[i])]
        i += 1
    return int(''.join([str(x) for x in result[0]]), base=2)

assert co2_scrub_rating(test_report) == 10

print(o2_gen_rating(report)*co2_scrub_rating(report))