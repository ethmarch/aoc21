# Part 1
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 
# where x1,y1 are the coordinates of one end the line segment and x2,y2
# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

from collections import namedtuple
from typing import Tuple, List


test_input = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''

Point = namedtuple('Point', ['x', 'y'])

def count_intersections(lines: List[Tuple]) -> int:
    line_points = {}
    for line in lines:
        if line[0].x == line[1].x:
            x = line[0].x
            mn = min(line[0].y, line[1].y)
            mx = max(line[0].y, line[1].y)
            for i in range(mn, mx+1):
                pt = Point(x, i)
                line_points[pt] = line_points.get(pt, 0) + 1
        elif line[0].y == line[1].y:
            y = line[0].y
            mn = min(line[0].x, line[1].x)
            mx = max(line[0].x, line[1].x)
            for i in range(mn, mx+1):
                pt = Point(i, y)
                line_points[pt] = line_points.get(pt, 0) + 1
        else:
            ordered = sorted(line, key=lambda n: n.x)
            slope = 1 if ordered[0].y < ordered[1].y else -1
            for i in range(ordered[0].x, ordered[1].x + 1):
                y = (slope * (i - ordered[0].x)) + ordered[0].y
                pt = Point(i, y)
                line_points[pt] = line_points.get(pt, 0) + 1
    
    return len([x for x in line_points.values() if x > 1])

def make_lines(input: str):
    return [tuple([Point(*[int(y) for y in x.split(',')]) for x in ln.split(' -> ')]) for ln in input.splitlines()]

test_lines = make_lines(test_input)
assert count_intersections(test_lines) == 12

with open('data/day05.txt', 'r') as f:
    raw = f.read()
    lines = make_lines(raw)
    print(count_intersections(lines))

# Part 2
# you need to also consider diagonal lines.
# Because of the limits of the hydrothermal vent mapping system, the lines 
# in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees.