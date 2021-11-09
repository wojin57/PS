def minimum_expense(city_info, expense_list, N):
    return min([expense_list[N - x[1]] + x[0] if N >= x[1] else x[0] for x in city_info])

if __name__ == '__main__':
    C, N = [int(x) for x in input().split()]
    city_info = [list(map(int, input().split())) for _ in range(N)]
    expense_list = [0 for _ in range(C)]
    for i in range(C):
        expense_list[i] = minimum_expense(city_info, expense_list, i)
    print(expense_list[C - 1])
