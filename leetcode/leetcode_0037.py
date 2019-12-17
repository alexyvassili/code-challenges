from typing import List
from itertools import product

base_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def get_ixes(i):
    ixes = {i}
    left_side = i % 3
    right_side = 2 - left_side
    for k in range(1, left_side + 1):
        ixes.add(i - k)
    for k in range(1, right_side + 1):
        ixes.add(i + k)
    return ixes


def get_square_indexes3x3(i, j):
    ixes = get_ixes(i)
    jxes = get_ixes(j)
    return product(ixes, jxes)


def switch_horizontal(board, i, j):
    existing_values = {board[i][jx] for jx in range(len(board[i])) if board[i][jx] != '.'}
    return base_set - existing_values


def switch_vertical(board, i, j):
    existing_values = {board[ix][j] for ix in range(len(board)) if board[ix][j] != '.'}
    return base_set - existing_values


def switch_square(board, i, j):
    square_indexes = get_square_indexes3x3(i, j)
    existing_values = {board[ix][jx] for ix, jx in square_indexes if board[ix][jx] != '.'}
    return base_set - existing_values


def switch_value(board, i, j):
    print('Indexes', i, j)
    values = switch_horizontal(board, i, j)
    values = values.intersection(switch_vertical(board, i, j))
    values = values.intersection(switch_square(board, i, j))
    print('Values', values)
    if len(values) == 1:
        return values.pop()
    return None


def solveSudoku(board: List[List[str]]) -> None:
    while True:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    
                    value = switch_value(board, i, j)
                    
                    if value:
                        board[i][j] = value
                        count += 1
        if not count:
            break
