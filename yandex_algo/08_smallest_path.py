from heapq import heappush, heappop


def get_successors(x, y, max_x, max_y):
    successors = []
    if x < max_x:
        successors.append((x + 1, y))
    if y < max_y:
        successors.append((x, y + 1))
    return successors


def a_star(start_coords, goal_coords, matrix):
    queue = []
    x, y = start_coords
    max_x = len(matrix) - 1
    max_y = len(matrix[-1]) - 1
    heappush(queue, (matrix[x][y], start_coords))
    iters = 0
    while queue:
        iters += 1
        weight, last_node = heappop(queue)
        if last_node == goal_coords:
            return weight, last_node, iters
        for succ_x, succ_y in get_successors(*last_node, max_x, max_y):
            succ_weigth = matrix[succ_x][succ_y]
            heappush(queue, (weight + succ_weigth, (succ_x, succ_y)))
    return "Error"


matrix = [
    [1, 1, 1, 1, 1],
    [3, 100, 100, 100, 100],
    [1, 1, 1, 1, 1],
    [2, 1, 2, 2, 2],
    [1, 1, 1, 1, 1]
]


matrix = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]


START = 0, 0
END = len(matrix) - 1, len(matrix[-1]) - 1

print(a_star(START, END, matrix))

from time import time
N = 3
for N in range(3, 30):
    matrix = []
    for i in range(N):
        matrix.append([i + j for j in range(N)])
        matrix.append(sorted([i + j for j in range(N)], reverse=True))
    from pprint import pprint
    # pprint(matrix)
    END = len(matrix) - 1, len(matrix[-1]) - 1
    t1 = time()
    res = a_star(START, END, matrix)[-1]
    t = time() - t1
    print(N, t * 1000)

# количество итераций
# на возрастающе - убывающих массивах и на единичках
# 3x3           50           63
# 4x4          260          375
# 5x5        1 339        2 288
# 6x6        7 013       14 196
# 7x7       35 647       89 148
# 8x8      187 707      564 927
# 9x9      981 815    3 605 250
# 10x10  5 263 873   23 138 115

# время выполнения, ms
# на возрастающе - убывающих массивах и на единичках
# 3x3         0.106      0.13
# 4x4         0.65       0.86
# 5x5          3          5
# 6x6         18         47
# 7x7        105        242
# 8x8        641      1 754
# 9x9      3 663     11 615
# 10x10   25 100     86 164

# на единичках

