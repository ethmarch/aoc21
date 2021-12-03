## Part 1

# Calculate the horizontal position and depth you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your final depth?

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

from collections import namedtuple
from typing import NamedTuple, Tuple, List

# point on a coordinate plane
# x is horizontal displacement
# y is depth (down +, up -)
Point = namedtuple('Point', ['x', 'y'])

class Sub:
    def __init__(self, posn: Point = Point(0,0)):
        self.posn = posn

    def forward(self, n: int):
        new_x = self.posn.x + n
        self.posn = Point(new_x, self.posn.y)

    def down(self, n: int):
        new_y = self.posn.y + n
        self.posn = Point(self.posn.x, new_y)

    def up(self, n: int):
        new_y = self.posn.y - n
        self.posn = Point(self.posn.x, new_y)

    def move(self, course: List[Tuple]):
        for step in course:
            self.__getattribute__(step[0])(step[1])

# A course is a list of tuples of the form (command, distance)

test_course = [('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)]
test_sub = Sub()
test_sub.move(test_course)
assert test_sub.posn == Point(15, 10)

with open('data/day2.txt', 'r') as f:
    parsed = [line.strip().split() for line in f.readlines()]
    course = [(a, int(b)) for a,b in parsed]
    sub = Sub()
    sub.move(course)
    print(sub.posn.x * sub.posn.y)

# Part 2

# In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0

#down X increases your aim by X units.
#up X decreases your aim by X units.
#forward X does two things:
#  - It increases your horizontal position by X units.
#  - It increases your depth by your aim multiplied by X

class Sub2:
    def __init__(self, posn: Point = Point(0,0), aim: int = 0):
        self.posn = posn
        self.aim = aim

    def forward(self, n: int):
        new_x = self.posn.x + n
        new_y = self.posn.y + (self.aim * n)
        self.posn = Point(new_x, new_y)

    def down(self, n: int):
        self.aim += n

    def up(self, n: int):
        self.aim -= n

    def move(self, course: List[Tuple]):
        for step in course:
            self.__getattribute__(step[0])(step[1])

test_course = [('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)]
test_sub2 = Sub2()
test_sub2.move(test_course)
assert test_sub2.posn == Point(15, 60)

with open('data/day2.txt', 'r') as f:
    parsed = [line.strip().split() for line in f.readlines()]
    course = [(a, int(b)) for a,b in parsed]
    sub = Sub2()
    sub.move(course)
    print(sub.posn.x * sub.posn.y)