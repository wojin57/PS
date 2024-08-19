# https://school.programmers.co.kr/learn/courses/30/lessons/258709
from itertools import combinations

# return the count of sum of dice below the target value
def binary_search(target, case):
    low = 0
    high = len(case) - 1

    while low <= high:
        mid = (low + high) // 2

        if case[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

# recursive function calculating the sum of dice
def simulate(case, dice, idx, now, out):
    if idx == len(case):
        out.append(now)
        return

    for d in dice[case[idx]]:
        simulate(case, dice, idx + 1, now + d, out)

def solution(dice):
    answer = []

    # combination of selecting dice
    half = len(dice) // 2
    selected_cases = list(combinations(list(range(len(dice))), half))

    # simulate each combination and calculate the results
    sum_cases = {}
    for idx, case in enumerate(selected_cases):
        out = []
        simulate(case, dice, 0, 0, out)
        out.sort() # sort for binary search
        sum_cases[idx] = out

    # find the maximum winning case
    best_sum = 0
    for key, value in sum_cases.items():
        # case for A
        case_A = value
        # case for B
        case_B = sum_cases[len(selected_cases) - key - 1]

        temp_sum = 0
        for c in case_A:
            temp_sum += binary_search(c, case_B)

        if temp_sum > best_sum:
            best_sum = temp_sum
            best_case = selected_cases[key]
            answer = list(map(lambda x : x + 1, sorted(best_case[:])))

    return answer