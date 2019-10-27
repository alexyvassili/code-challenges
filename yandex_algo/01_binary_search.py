"""Дан сортированный в возрастающем порядке массив целых чисел
    nums из n элементов и число target.
    Напишите функцию для поиска target в nums.
    Если target существует, верните его индекс,
    иначе верните -1.
    1. n лежит в границах [1, 10000]
    2. Каждый элемент лежит в границах [-9999, 9999]
"""


def binary_search(nums, target):
    begin = 0
    end = len(nums) - 1
    while True:
        target_ix = (begin + end) // 2
        if nums[target_ix] == target:
            return target_ix
        if begin == end:
            return -1
        if target > nums[target_ix]:
            begin = target_ix + 1
        elif target < nums[target_ix]:
            end = target_ix - 1 if target_ix else 0
