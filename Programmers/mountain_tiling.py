# https://school.programmers.co.kr/learn/courses/30/lessons/258705
# Divide & Conquer
def solution(n, tops):
    a, b, s = 2 + tops[0], 1, 3 + tops[0]
    for t in tops[1:]:
        a = (2 + t) * a + (1 + t) * b
        b = s
        s = a + s
    return s % 10007

if __name__ == '__main__':
    print(solution(4, [1, 1, 0, 1]))