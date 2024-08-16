# https://school.programmers.co.kr/learn/courses/30/lessons/161988
# Kadane's algorithm: O(N) algorithm for solving maximum subsequnce problem(only for the sum value)
def kadane_algorithm(sequence):
    global_sum = sequence[0]
    local_sum = sequence[0]
    for item in sequence[1:]:
        local_sum = max(item, local_sum + item)
        global_sum = max(global_sum, local_sum)
        
    return global_sum


def solution(sequence):
    # Solve the maximum subsequence problem for each 1, -1 pulse sequence
    pos_seq = [sequence[i] * pow(-1, i) for i in range(len(sequence))]
    neg_seq = [pos_seq[i] * (-1) for i in range(len(pos_seq))] # using list comprehension to shorten the code
    return max(kadane_algorithm(pos_seq), kadane_algorithm(neg_seq))
    