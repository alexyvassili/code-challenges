def reverse(integer):
    sign = 1 if integer >= 0 else -1
    reversed_ = int(str(abs(integer))[::-1]) * sign
    if (integer < 2 ** 31 - 1) or integer > 2 ** 31:
        return 0
    if (reversed_ < 2 ** 31 - 1) or reversed_ > 2 ** 31:
        return 0
    return reversed_
