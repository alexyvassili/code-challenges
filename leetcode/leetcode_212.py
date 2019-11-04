"""Задача - дана доска с буквами и слова - вернуть слова,
    которые есть на доске
"""

class Route:
    def __init__(self, start_coord):
        self._route = {start_coord}
        self.tail = start_coord
    
    def update(self, coord):
        new_route = Route(coord)
        new_route._route.update(self._route)
        return new_route
    
    def __contains__(self, coord):
        return coord in self._route
    
    def __repr__(self):
        return str(self._route)


def is_valid_coord(x, y, board):
    return ((0 <= x < len(board)) and
            (0 <= y < len(board[x])))


def get_nearest_coords(x, y, board):
    nearest_coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for coord in nearest_coords:
        if is_valid_coord(*coord, board):
            yield coord
    

def get_near_char_coord(current_coord, char, board):
    for x, y in get_nearest_coords(*current_coord, board):
        if board[x][y] == char:
            yield x, y


def update_route(route, char, board):
    new_routes = []
    current_coord = route.tail
    for coord in get_near_char_coord(current_coord, char, board):
        if coord not in route:
            new_routes.append(route.update(coord))
    return new_routes


def update_routes(routes, char, board):
    updated_routes = []
    for route in routes:
        updated_routes += update_route(route, char, board)
    return updated_routes


def get_char_coords(char, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == char:
                yield i, j


def init_routes(char, board):
    routes = []
    for coord in get_char_coords(char, board):
        routes.append(Route(coord))
    return routes


def is_word_on_board(word, board, letters):
    if set(word) - letters:
        return False
    
    routes = init_routes(word[0], board)
    i = 1
    while routes:
        print(len(routes))
        if i >= len(word):
            break
        routes = update_routes(routes, word[i], board)
        i += 1
    
    return bool(routes)


def find_words_on_board(words, board):
    letters = {char for row in board for char in row}
    return [word for word in words if is_word_on_board(word, board, letters)]


if __name__ == "__main__":
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'w']
    ]
    
    words = ["oath", "pea", "eat", "rain"]
    
    
    board = [["a","a","a","a"],
             ["a","a","a","a"],
             ["a","a","a","a"],
             ["a","a","a","a"],
             ["b","c","d","e"],
             ["f","g","h","i"],
             ["j","k","l","m"],
             ["n","o","p","q"],
             ["r","s","t","u"],
             ["v","w","x","y"],
             ["z","z","z","z"]]
    
    words = ["aaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaab","aaaaaaaaaaaaaaac",]
    from time import time
    t1 = time()
    print(find_words_on_board(words, board))
    t2 = time()
    print('time:', t2-t1)
