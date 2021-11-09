def dp(rgb_table, price_table, idx):
    if idx == 0:
        return rgb_table[0]
    
    price_red = rgb_table[idx][0] + min(price_table[idx - 1][1], price_table[idx - 1][2])
    price_green = rgb_table[idx][1] + min(price_table[idx - 1][0], price_table[idx - 1][2])
    price_blue = rgb_table[idx][2] + min(price_table[idx - 1][0], price_table[idx - 1][1])
    return [price_red, price_green, price_blue]


if __name__ == '__main__':
    N = int(input())
    rgb_table = [list(map(int, input().split())) for _ in range(N)]
    price_table = [[0, 0, 0] for _ in range(N)]
    for i in range(N):
        price_table[i] = dp(rgb_table, price_table, i)
    print(min(price_table[N - 1]))
