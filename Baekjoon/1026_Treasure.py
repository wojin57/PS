def find_minimum_S(N, A, B):
    A.sort()
    B.sort(reverse=True)
    return sum([A[i] * B[i] for i in range(N)])


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    print(find_minimum_S(N, A, B))
