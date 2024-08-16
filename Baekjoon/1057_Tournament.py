import math

def rounding(n):
    return math.ceil(n / 2)


def is_encounter(a, b):
    if (b - a == 1 and a % 2):
        return True
    else:
        return False


if __name__ == '__main__':
    N, a, b = [int(x) for x in input().split()]
    round = 1
    a, b = min(a, b), max(a, b)
    while (not is_encounter(a, b)):
        a = rounding(a)
        b = rounding(b)
        round += 1

    print(round)
