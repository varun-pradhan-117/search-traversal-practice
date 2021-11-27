from typing import List, Tuple, Dict
from enum import Enum, unique, auto

@unique
class Direction(Enum):
    NONE = auto()
    UP = auto()
    LEFT = auto()
    RIGHT = auto()
    DOWN = auto() 


def printBoard(board: List[List[chr]]) -> None:
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()


def heuristic_function(board: List[List[chr]], goalBoard: List[List[chr]]) -> int:
    mistake = 0
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            mistake += int(board[y][x] != goalBoard[y][x])
    return mistake


def find_blank(board: List[List[chr]]) -> Tuple[int, int]:
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == '0':
                return x, y


def best_first_search(board: List[List[chr]], goalBoard: List[List[chr]], previous: Direction) -> None:
    print(f"{previous}:")
    printBoard(board)
    print()

    (x, y) = find_blank(board)
    hd: List[Tuple[Direction, int]] = []

    # Left
    if x > 0 and previous is not Direction.RIGHT:
        board[y][x - 1], board[y][x] = board[y][x], board[y][x - 1]
        hd.append((Direction.LEFT, heuristic_function(board, goalBoard)))
        board[y][x - 1], board[y][x] = board[y][x], board[y][x - 1]

    # Up
    if y > 0 and previous is not Direction.DOWN:
        board[y - 1][x], board[y][x] = board[y][x], board[y - 1][x]
        hd.append((Direction.UP, heuristic_function(board, goalBoard)))
        board[y - 1][x], board[y][x] = board[y][x], board[y - 1][x]

    # Right
    if x < 2 and previous is not Direction.LEFT:
        board[y][x + 1], board[y][x] = board[y][x], board[y][x + 1]
        hd.append((Direction.RIGHT, heuristic_function(board, goalBoard)))
        board[y][x + 1], board[y][x] = board[y][x], board[y][x + 1]

    # Down
    if y < 2 and previous is not Direction.UP:
        board[y + 1][x], board[y][x] = board[y][x], board[y + 1][x]
        hd.append((Direction.DOWN, heuristic_function(board, goalBoard)))
        board[y + 1][x], board[y][x] = board[y][x], board[y + 1][x]

    hd.sort(key=lambda x: x[1])

    # Get the minimum heuristic, this allows backtracking
    minheuristic = hd[0][1]
    # eliminate every hscore greater than minimum heuristic
    hd = [(direction, hscore) for (direction, hscore) in hd if hscore <= minheuristic]

    for path in hd:

        direction, hscore = path

        # Change board as per selected direction
        if direction is Direction.LEFT:
            board[y][x - 1], board[y][x] = board[y][x], board[y][x - 1]

        elif direction is Direction.UP:
            board[y - 1][x], board[y][x] = board[y][x], board[y - 1][x]

        elif direction is Direction.RIGHT:
            board[y][x + 1], board[y][x] = board[y][x], board[y][x + 1]

        elif direction is Direction.DOWN:
            board[y + 1][x], board[y][x] = board[y][x], board[y + 1][x]

        if (hscore == 0):
            print(f"{direction}:")
            printBoard(board)
            print()
            return True
        if best_first_search(board, goalBoard, direction):
            return True
    return False



def main():
    board: List[List[chr]] = [
        ["2", "8", "3"],
        ["1", "6", "4"],
        ["7", "0", "5"]
    ]

    goalBoard = [
        ['1', '2', '3'],
        ['8', '0', '4'],
        ['7', '6', '5']
    ]
    
    best_first_search(board, goalBoard, Direction.NONE)


if __name__ == '__main__':
    main()