"""Определить корректность скобочной последовательности типа [{}[]]"""

OPEN_BRACKETS = "([{"
CLOSE_BRACKETS = {
    "}": "{",
    "]": "[",
    ")": "("
}


def check_brackets(string):
    brackets_stack = list()
    for s in string:
        if s in OPEN_BRACKETS:
            brackets_stack.append(s)
        elif s in CLOSE_BRACKETS:
            if brackets_stack and brackets_stack[-1] == CLOSE_BRACKETS[s]:
                brackets_stack.pop()
            else:
                return False
    if brackets_stack:
        return False
    return True

