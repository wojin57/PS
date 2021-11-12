import math

def calculate_probability(n, m, k):
    return sum([math.comb(m, i) * math.comb(n - m, m - i) for i in range(k, m + 1)]) / math.comb(n, m)


if __name__ == '__main__':
    N, M, K = [int(x) for x in input().split()]
    print(calculate_probability(N, M, K))
