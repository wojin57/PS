def add_bottles(N, K): # using bit operations, get sol in one operation
    sol = 0
    while format(N, 'b').count('1') > K:
        N += 1
        sol += 1

    return sol


if __name__ == '__main__':
    N, K = [int(x) for x in input().split()]
    print(add_bottles(N, K))
    