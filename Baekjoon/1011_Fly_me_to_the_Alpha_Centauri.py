import math

def least_split(n, m): # least number of split n into less than m
    if n == 0:
        return 0
    
    result = 1
    while (n > m):
        n -= m
        result += 1
    
    return result


def least_operation(l):
    dist = l[1] - l[0]
    max_move = math.floor(math.sqrt(float(dist))) # maximum sqaure number less than dist
    return 2 * max_move - 1 + least_split(dist - pow(max_move, 2), max_move)


if __name__ == '__main__':
    T = int(input())
    input_list = list()
    for _ in range(T):
        input_list.append([int(x) for x in input().split()])
    
    for i in range(T):
        print(least_operation(input_list[i]))
