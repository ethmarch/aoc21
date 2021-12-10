from typing import List, Tuple

# Part 1
# In the output values, how many times do digits 1, 4, 7, or 8 appear?

# seven-segment representation counts
# 2: 1
# 3: 7
# 4: 4
# 5: 2,3,5
# 6: 0,6,9
# 7: 8

test_raw = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''

def parse_input(raw: str) -> List[Tuple]:
    splits = [line.split('|') for line in raw.splitlines()]
    return [(x.strip().split(), y.strip().split()) for x,y in splits]

test_parsed = parse_input(test_raw)

def count_unique_rep_digits(input: List[str]) -> int:
    unique_reps = {2, 3, 4, 7}
    return sum([sum([len(y) in unique_reps for y in x]) for x in input])

test_outputs = [x[1] for x in test_parsed]
assert count_unique_rep_digits(test_outputs) == 26

with open('data/day08.txt', 'r') as f:
    raw = f.read()
    parsed = parse_input(raw)
    outputs = [x[1] for x in parsed]
    print(count_unique_rep_digits(outputs))

# Part 2
# What do you get if you add up all of the output values?


def create_mapping(input: List[str]) -> dict:
    mapping = {}
    unique_lengths = {2: 1, 3: 7, 4: 4, 7: 8}
    uniques = {}
    for segments in input:
        if len(segments) in unique_lengths:
            mapping[segments] = str(unique_lengths[len(segments)])
            uniques[unique_lengths[len(segments)]] = segments

    lookup = {'0101': '0', '1212': '2', '0102': '3', '1112': '5', '1111': '6', '0001': '9'}

    diff = lambda x,y: str(len(set(x).difference(y)))

    for seg in input:
        if seg not in mapping:
            lookup_key = ''.join([diff(uniques[x], seg) for x in [1,4,7,8]])
            mapping[seg] = lookup[lookup_key]

    return mapping

def find_sum(input: List[Tuple]) -> int:
    total = 0
    for entry in input:
        digits = [''.join(sorted(x)) for x in entry[0]]
        outputs = [''.join(sorted(x)) for x in entry[1]]
        mapping = create_mapping(digits)
        print(mapping)
        total += int(''.join([mapping[x] for x in outputs]))
    
    return total

assert find_sum(test_parsed) == 61229

with open('data/day08.txt', 'r') as f:
    raw = f.read()
    parsed = parse_input(raw)
    print(find_sum(parsed))