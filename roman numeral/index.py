def to_roman(num):
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman = ""
    for val, sym in roman_map:
        while num >= val:
            roman += sym
            num -= val
    return roman

n = int(input("Enter number: "))
print("Roman:", to_roman(n))
