# Part 1
# count the number of times a depth measurement increases from the previous measurement.

def count_increases(depths: list[int]) -> int:
    counter = 0
    for i in range(len(depths)-1):
        if depths[i+1] > depths[i]:
            counter += 1
    return counter

example_depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

assert count_increases(example_depths) == 7

with open('data/day1/part1.txt', 'r') as f:
    depths = [int(x.strip()) for x in f.readlines()]
    print(count_increases(depths))

# Part 2
# consider sums of a three-measurement sliding window
# count the number of times the sum of measurements in this sliding window increases

def windowed_increases(depths: list[int]) -> int:
    counter = 0
    for i in range(len(depths)-3):
        if depths[i] < depths[i+3]: # windows will always share the middle 2 values, only need to compare the edges
            counter += 1
    return counter

assert windowed_increases(example_depths) == 5

with open('data/day1/part1.txt', 'r') as f:
    depths = [int(x.strip()) for x in f.readlines()]
    print(windowed_increases(depths))


# Prettier solutions using zip found elsewhere
# Nice trick to remember
def part1(depths):
    pairs = zip(depths, depths[1:])
    return sum([a < b for a,b in pairs])

assert part1(example_depths) == 7

def part2(depths):
    windows = list(zip(depths, depths[1:], depths[2:]))
    pairs = zip(windows, windows[1:])
    return sum([sum(a) < sum(b) for a,b in pairs])

assert part2(example_depths) == 5