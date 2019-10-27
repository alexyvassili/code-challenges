"""Даны строка S и паттерн P для поиска в этой строке.
    Определите, содержатся ли символы паттерна P в строке S.
    Паттерн не обязан быть подстрокой.
"""


def pattern_search(line, pattern):
    ix = 0
    for char in line:
        if char == pattern[ix]:
            ix += 1
        if ix == len(pattern):
            return True
    return False
