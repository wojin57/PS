# https://school.programmers.co.kr/learn/courses/30/lessons/181186
def solution(n):
    DIV = 1000000007
    # an: total number of posibbilities, bn: total number of stair-like placements
    # an = an-1 + 2an-2 + 5an-3 + bn
    # bn = 2an-3 + 2an-4 + 4an-5 + ...
    # summarized as an = an-1 + 2an-2 + 6an-3 + an-4 - an-6
    answer = [1, 1, 3, 10, 23, 62, 170]
    if n < 7:
        return answer[n]
    answer = answer + [0] * (n - 6)
    
    for i in range(5, n + 1):
        answer[i] = answer[i - 1] + 2 * answer[i - 2] + 6 * answer[i - 3] + answer[i - 4] - answer[i - 6]
    return answer[-1] % DIV
    

if __name__ == '__main__':
    print(solution(12))