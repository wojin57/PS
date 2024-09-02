# https://school.programmers.co.kr/learn/courses/30/lessons/132266
def solution(n, roads, sources, destination):
    answer = []
    distance = [-1] * (n + 1)
    distance[destination] = 0
    queue = [destination]
    graph = [[] for _ in range(n + 1)]
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    while queue:
        cur = queue.pop(0)
        remove_dest = []
        for dest in graph[cur]:
            if distance[dest] == -1:
                queue.append(dest)
                distance[dest] = distance[cur] + 1
                remove_dest.append(dest)
            
        for dst in remove_dest:
            graph[cur].remove(dst)
            graph[dst].remove(cur)
                     
    for s in sources:
        answer.append(distance[s])
    
    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))