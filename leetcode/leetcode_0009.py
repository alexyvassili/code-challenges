import math

def is_palindrome(x):
    s = x
    if x < 0:
        return False
    if 0 <= x < 10:
        return True
    
    y = 0
    while x:
        y, x = y + x % 10, x // 10
        y *= 10
    y = y // 10
    return s == y


print(is_palindrome(9010109))
print(is_palindrome(22))
print(is_palindrome(546424649))
print(is_palindrome(546424645))