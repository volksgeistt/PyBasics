import random

def random_color():
    return '#' + ''.join(random.choices('0123456789ABCDEF', k=6))

print("Hex Code:", random_color())
