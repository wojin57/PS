# https://school.programmers.co.kr/learn/courses/30/lessons/258707
# return True and remove any pair if exists, return False elsewhere.
def pair_check(hands, n):
    for i, a in enumerate(hands):
        for b in hands[i + 1:]:
            if a + b == n + 1:
                hands.remove(a)
                hands.remove(b)
                return True
    return False


# return True if target's pair is exists in hands
def target_pair(hands, target, n):
    return n + 1 - target in hands


def solution(coin, cards):
    answer = 0
    n = len(cards)
    hands = cards[:n//3]
    draws = []
    # hand: n / 3, 2 for each round
    # max round: n / 2
    # card drawable round: n / 3
    is_valid = True
    while is_valid and answer <= n // 3:
        if answer < n // 3:
            # we can "lazily" choose to draw cards
            draws = draws + [cards[n // 3 + 2 * answer], cards[n // 3 + 2 * answer + 1]]
        answer += 1
        is_valid = False
        
        # draw only if it is needed
        if pair_check(hands, n):
            is_valid = True
            continue
        elif coin > 0:
            # draw one card if its pair is in hands
            for t in draws:
                if target_pair(hands, t, n):
                    coin -= 1
                    hands.remove(n + 1 - t)
                    draws.remove(t)
                    is_valid = True
                    break
            # for worst case, draw two cards
            if not is_valid and coin > 1 and pair_check(draws, n):
                coin -= 2
                is_valid = True
                continue
        
    return answer


if __name__ == '__main__':
    print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))