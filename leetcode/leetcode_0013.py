def roman2integer(rom):
    roman = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    rom = rom[::-1]
    num = roman[rom[0]]
    last_num = num
    for r in rom[1:]:
        cur_num = roman[r]
        if cur_num < last_num:
            num -= cur_num
        else:
            num += cur_num
        last_num = cur_num
    return num

print(
    roman2integer("MDCCIX")
)