def get_max_length(arr):
    max_len = 0
    for lst in arr:
        for x in lst:
            if len(str(x)) > max_len:
                max_len = len(str(x))

    return max_len


def get_value(row, col):
    lap = max(map(abs, [row, col]))
    init_value = pow(2 * lap - 1, 2)
    if col == lap: # case 1. up
        if row == lap:
            order = 8 * lap
        else:
            order = lap - row
    elif row == -lap: # case 2. left
        order = 3 * lap - col
    elif col == -lap: # case 3. down
        order = 5 * lap + row
    else: # case 4. right
        order = 7 * lap + col
    return init_value + order


def set_whirlpool(r1, c1, r2, c2, arr):
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            arr[i - r1][j - c1] = get_value(i, j)


def print_whirlpool(arr):
    # get number_max_length
    number_max_length = get_max_length(arr)
    row_length = len(arr)
    col_length = len(arr[0])
    # print the array in right manner
    for i in range(row_length):
        for j in range(col_length):
            print(f'{arr[i][j]:{number_max_length}d}', end=' ')
        print()


if __name__ == '__main__':
    r1, c1, r2, c2 = [int(x) for x in input().split()]
    # max_lap = max(map(abs, [r1, c1, r2, c2]))
    whirlpool = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
    set_whirlpool(r1, c1, r2, c2, whirlpool)
    print_whirlpool(whirlpool)
