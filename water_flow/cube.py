from collections import namedtuple


GRUND = 5
WATER = 15
AIR = 25

Coords = namedtuple("Coords", "w l")


class CubeSlice:
    def __init__(self, data, level):
        self.level = level
        self.width = len(data)
        self.length = len(data[0])
        self.shape = (self.width, self.length)
        self._slice = [[GRUND if level < h else WATER for h in row]
                       for row in data]

    def is_valid_coords(self, coords: Coords):
        w, l = coords
        return (0 <= w < self.width) and (0 <= l < self.length)

    def items(self):
        return ((Coords(w, l), self._slice[w][l])
                for w in range(self.width) for l in range(self.length))

    def count(self, value):
        count = 0
        for w in range(self.width):
            for l in range(self.length):
                if self._slice[w][l] == value:
                    count += 1
        return count

    def __setitem__(self, key: Coords, value):
        w, l = key
        self._slice[w][l] = value

    def __getitem__(self, key: Coords):
        w, l = key
        return self._slice[w][l]

    def __repr__(self):
        return f'<CubeSlice level {self.level}>'


class Cube:
    def __init__(self, data):
        self.height = self.get_height(data)
        self.width = self.get_width(data)
        self.length = self.get_length(data)
        self.slices = [CubeSlice(data, level) for level in range(self.height)]
        self._iter_index = 0

    @staticmethod
    def get_height(data):
        return max(max(row) for row in data)

    @staticmethod
    def get_width(data):
        return len(data)

    @staticmethod
    def get_length(data):
        lengths = {len(row) for row in data}
        if len(lengths) > 1:
            raise ValueError("Data has inconsistent length")
        return list(lengths)[0]

    def count(self, value):
        return sum(cube_slice.count(value) for cube_slice in self.slices)

    def __iter__(self):
        return self

    def __next__(self):
        current_index = self._iter_index
        if current_index >= len(self.slices):
            self._iter_index = 0
            raise StopIteration
        self._iter_index += 1
        return self.slices[current_index]
