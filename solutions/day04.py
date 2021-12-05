from typing import List, Tuple

'''
The score of the winning board can now be calculated. Start by finding the sum of all 
unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum 
by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. 
What will your final score be if you choose that board?
'''

raw_test = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''

BOARD_SIZE = 5

class Cell:
    def __init__(self, value: int, above=None, right=None, below=None, left=None):
        self.value = value
        self.above = above
        self.right = right
        self.below = below
        self.left = left
        self.marked = False

    def update_neighbors(self, above=None, right=None, below=None, left=None):
        self.above = above or self.above
        self.right = right or self.right
        self.below = below or self.below
        self.left = left or self.left
        return self

    def __str__(self):
        return f'Value: {self.value} Marked: {self.marked}'
       
    def __repr__(self):
        return f'Value: {self.value} Marked: {self.marked}'

    def dir_marked(self, direction: str):
        dir = self.__getattribute__(direction)
        if dir and dir.marked:
            return 1 + dir.dir_marked(direction)
        else:
            return 0

    def check_win(self):
        if self.marked:
            vert = (self.dir_marked('above') + self.dir_marked('below')) == (BOARD_SIZE - 1)
            horz = (self.dir_marked('right') + self.dir_marked('left')) == (BOARD_SIZE - 1)
            return vert or horz
        else:
            return False


def parse_input(raw: str) -> Tuple:
    lines = raw.splitlines()
    calls = [int(n) for n in lines[0].split(',')]
    boards = []
    current_board = []
    for line in lines[2:]:
        if line:
            current_board.append([Cell(int(n)) for n in line.split()])
        else:
            boards.append(current_board)
            current_board = []
    boards.append(current_board)
    return (calls, boards)

test_calls, test_boards = parse_input(raw_test)

assert len(test_calls) == 27
assert len(test_boards) == 3
assert len(test_boards[0]) == 5
assert len(test_boards[0][0]) == 5

def build_board(raw_board: List[List[Cell]]):
    board = {}
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            above = raw_board[i-1][j] if i > 0 else None
            right = raw_board[i][j+1] if j < BOARD_SIZE - 1 else None
            below = raw_board[i+1][j] if i < BOARD_SIZE - 1 else None
            left = raw_board[i][j-1] if j > 0 else None
            raw_board[i][j].update_neighbors(above, right, below, left)
            board[raw_board[i][j].value] = raw_board[i][j]
    return board

assert len(build_board(test_boards[0]).items()) == 25

print(build_board(test_boards[0])[14])

def first_winner(calls, boards):
    winner = None
    last_called = None
    for call in calls:
        if winner:
            break
        last_called = call
        for board in boards:
            if winner:
                break
            cell = board.get(call)
            if cell:
                cell.marked = True
                winner = board if cell.check_win() else None
    
    unmarked_sum = sum([x.value for x in winner.values() if not x.marked])

    return unmarked_sum * last_called

test_boards = [build_board(x) for x in test_boards]

assert first_winner(test_calls, test_boards) == 4512

with open('data/day04.txt', 'r') as f:
    raw = f.read()
    calls, boards = parse_input(raw)
    built_boards = [build_board(x) for x in boards]
    print(first_winner(calls, built_boards))


# Part 2
# figure out which board will win last and choose that one

def last_winner(calls, boards):
    winners = [False] * len(boards)
    for call in calls:
        if sum(winners) == len(boards):
            break
        last_called = call
        for i, board in enumerate(boards):
            if sum(winners) == len(boards):
                break
            last_board = board
            cell = board.get(call)
            if cell:
                cell.marked = True
                winners[i] = winners[i] or cell.check_win()
    
    unmarked_sum = sum([x.value for x in last_board.values() if not x.marked])
    return unmarked_sum * last_called

assert last_winner(test_calls, test_boards) == 1924

with open('data/day04.txt', 'r') as f:
    raw = f.read()
    calls, boards = parse_input(raw)
    built_boards = [build_board(x) for x in boards]
    print(last_winner(calls, built_boards))