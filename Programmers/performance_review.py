# https://school.programmers.co.kr/learn/courses/30/lessons/152995
def solution(scores):
    answer = 1
    target_a, target_b = scores[0]
    target_score = target_a + target_b
    
    # ascending sort for first element, descending sort for second element
    # ensures that we need O(n) search only
    scores.sort(key=lambda x: (-x[0], x[1]))
    max_b = 0
    
    for a, b in scores:
        # ankle breaker
        if target_a < a and target_b < b:             
            return -1
        
        # candidate for upper rankers
        if b >= max_b:
            max_b = b
            if a + b > target_score:
                answer += 1
    
    return answer


if __name__ == '__main__':
    print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))