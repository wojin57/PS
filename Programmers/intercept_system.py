# https://school.programmers.co.kr/learn/courses/30/lessons/181188
def solution(targets):
    answer = 0
    # find maximum number of unoverlapped missiles
    targets.sort(key=lambda a:a[1]) # ascending order sort using e
    e = 0
    for ts, te in targets:
        if e <= ts:
            e = te
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))