import random as rd

def heur(queens):
    h = 0
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i] == queens[j]:
                h += 1
            offset = j - i

            if queens[i] == queens[j] - offset or queens[i] == queens[j] + offset:
                h += 1
    return h


def NQueens(queens):
    moves = {}
    for col in range(len(queens)):
        best_move = queens[col]

        for row in range(len(queens)):
            if queens[col] == row:
                continue

            board_copy = list(queens)
            board_copy[col] = row
            moves[(col, row)] = heur(board_copy)

    best_moves = []
    best_h = heur(queens)
    for (i, j) in moves.items():
        if j < best_h:
            best_h = j

    for i, j in moves.items():
        if j == best_h:
            best_moves.append(i)

    if len(best_moves) > 0:
        pick = rd.randint(0, len(best_moves) - 1)
        col, row = best_moves[pick]
        queens[col] = row
    return queens


if __name__ == '__main__':
    n=int(input("Enter n:"))
    queens = [0 for i in range(n)]
    while heur(queens) != 0:
        NQueens(queens)

    board = [[0 for _ in range(n)] for _ in range(n)]

    for row, col in enumerate(queens):
        board[row][col] = 1
    
    for row in board:
        print(row)
