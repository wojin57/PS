# https://school.programmers.co.kr/learn/courses/30/lessons/42839
import math
import itertools

def is_prime(primes, num):
    if num < 3163 and primes[num] is not None:
        return primes[num]
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if primes[i] and num % i == 0:
            return False
        
    return True
    

def solution(numbers):
    answer = set()
    primes = [None for _ in range(3163)] # sqrt(9999999)~3162.27
    primes[0] = False
    primes[1] = False
    primes[2] = True
    
    for i in range(3, 3163):
        primes[i] = is_prime(primes, i)
        
    for l in range(1, len(numbers) + 1):
        for num in itertools.permutations(numbers, l):
            num = int("".join(num))
            if is_prime(primes, num):
                answer.add(num)
    
    return len(answer)


if __name__ == '__main__':
    print(solution("17"))