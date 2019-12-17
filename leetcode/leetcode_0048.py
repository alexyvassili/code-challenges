"""Rotate image"""


def rotate_perimeter(image, startxy, lastxy):
    print('#########')
    print('Startxy', startxy, 'Lastxy', lastxy)
    for delta in range(lastxy - startxy):
        print('Delta', delta)
        print(f"{startxy},{startxy+delta} -> {startxy+delta},{lastxy} -> {lastxy},{lastxy-delta} -> {lastxy-delta},{startxy} -> ")
        # first coord - y, second coord - x
        image[startxy][startxy + delta], image[startxy + delta][lastxy], image[lastxy][lastxy-delta], image[lastxy-delta][startxy] = image[lastxy-delta][startxy], image[startxy][startxy + delta], image[startxy + delta][lastxy], image[lastxy][lastxy-delta] 


def rotate(image):
    startxy = 0
    lastxy = len(image) - 1
    while startxy <= lastxy:
        rotate_perimeter(image, startxy, lastxy)
        startxy += 1
        lastxy -= 1


image = [
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35]
]

# image = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
# ]

from pprint import pprint
pprint(image)
print()
rotate(image)
pprint(image)
