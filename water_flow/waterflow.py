"""Задача: на острове идет дождь. Определить сколько воды
    останется на местности. Дается матрица высот.

    Решение: заполняем весь куб водой и потом решаем,
    из какого квадрата вода вытечет.
    В кубе у каждой ячейки три состояния: грунт, вода и воздух
    цифры выбраны чтобы было удобнее рисовать в matplotlib
    Измерения матрицы:
        ^ 1  2  3  4  3  2
        w 1  2  3  4  3  2
        i 1  2  3  4  3  2
        d 1  2  3  4  3  2
        t 1  2  3  4  3  2
        h 1  2  3  4  3  2
           l e n g t h ->
"""
from cube import Cube, CubeSlice, WATER, AIR, Coords


def get_perimeter_coords(width, length):
    perimeter_coords = set()
    perimeter_coords.update(Coords(0, i) for i in range(length))
    perimeter_coords.update(Coords(width-1, i) for i in range(length))
    perimeter_coords.update(Coords(i, 0) for i in range(width))
    perimeter_coords.update(Coords(i, length-1) for i in range(width))
    return perimeter_coords


def check_perimeter(cube_slice: CubeSlice):
    perimeter_coords = get_perimeter_coords(*cube_slice.shape)
    for coord in perimeter_coords:
        if cube_slice[coord] == WATER:
            cube_slice[coord] = AIR


def get_water_and_air_cells(cube_slice: CubeSlice):
    coords_by_water, coords_by_air = set(), set()
    for coords, value in cube_slice.items():
        if value == WATER:
            coords_by_water.add(coords)
        elif value == AIR:
            coords_by_air.add(coords)
    return coords_by_water, coords_by_air


def get_near_coords(coords, cube_slice):
    near_coords = [
        Coords(coords.w + 1, coords.l),
        Coords(coords.w - 1, coords.l),
        Coords(coords.w, coords.l + 1),
        Coords(coords.w, coords.l - 1),
    ]
    return (coord for coord in near_coords if cube_slice.is_valid_coords(coord))


def is_air_near(coords: Coords, cube_slice: CubeSlice):
    for crd in get_near_coords(coords, cube_slice):
        if cube_slice[crd] == AIR:
            return True
    return False


def water_flow_step(coords_by_water: set, coords_by_air: set, cube_slice: CubeSlice):
    count = 0
    for coords in list(coords_by_water):
        if is_air_near(coords, cube_slice):
            coords_by_water.remove(coords)
            coords_by_air.add(coords)
            cube_slice[coords] = AIR
            count += 1
    return count


def water_flow_on_slice(cube_slice: CubeSlice):
    coords_by_water, coords_by_air = get_water_and_air_cells(cube_slice)
    while water_flow_step(coords_by_water, coords_by_air, cube_slice):
        pass


def water_flow(data: list):
    cube = Cube(data)
    for cube_slice in cube:
        check_perimeter(cube_slice)
        water_flow_on_slice(cube_slice)
    return cube.count(WATER)


if __name__ == "__main__":
    # создаем остров 9х9
    data = [
        [1, 1, 1, 1, 1, 2, 3, 2, 1],
        [1, 0, 0, 2, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 1, 0, 2],
        [1, 3, 4, 4, 3, 3, 2, 0, 3],
        [2, 0, 0, 5, 0, 0, 2, 0, 4],
        [3, 5, 4, 3, 3, 3, 3, 2, 2],
        [4, 0, 0, 0, 0, 0, 3, 0, 1],
        [5, 0, 0, 0, 0, 0, 3, 0, 1],
        [4, 3, 2, 1, 1, 2, 3, 2, 1],
    ]

    # data = [
    #     [1, 1, 1, 1, 1, 2, 3, 2, 1],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 2],
    #     [2, 0, 0, 0, 0, 0, 0, 0, 2],
    #     [1, 0, 5, 5, 5, 0, 0, 0, 3],
    #     [2, 0, 5, 0, 5, 0, 0, 0, 4],
    #     [3, 0, 5, 0, 5, 0, 0, 0, 2],
    #     [4, 0, 5, 5, 5, 0, 0, 0, 1],
    #     [5, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [4, 3, 2, 1, 1, 2, 3, 2, 1],
    # ]

    c = Cube(data)
    print(
        water_flow(data)
    )
