from collections import deque


def solution(n, computers):
    """
    DFS/BFS 알고리즘 문제 - '네트워크' - 프로그래머스
    """
    answer = 0
    visited = [0] * n

    for i in range(n):
        if visited[i] != 1:
            answer += bfs(i, visited, computers, n)

    return answer


def bfs(idx, visited, computers, n):
    queue = deque()
    queue.append(idx)

    while queue:
        idx = queue.popleft()
        visited[idx] = 1
        network = computers[idx]

        for j in range(0, n):
            if j == idx:
                continue
            if network[j] == 1 and visited[j] == 0:
                queue.append(j)

    return 1
