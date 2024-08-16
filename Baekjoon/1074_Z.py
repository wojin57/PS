def find_order(N, r, c):
    if N == 1:
        return 2 * r + c
    
    loc_order = pow(pow(2, N - 1), 2)
    loc_adjust = pow(2, N - 1)
    if r < pow(2, N - 1) and c < pow(2, N - 1):
        loc_order *= 0
    elif r < pow(2, N - 1) and c >= pow(2, N - 1):
        c -= loc_adjust
    elif c < pow(2, N - 1):
        loc_order *= 2
        r -= loc_adjust 
    else:
        loc_order *= 3
        r -= loc_adjust
        c -= loc_adjust
        
    return loc_order + find_order(N - 1, r, c)


if __name__ == '__main__':
    N, r, c = [int(x) for x in input().split()]
    print(find_order(N, r, c))
