def solution(numbers, target):
    """
    DFS/BFS 문제 - '타겟 넘버' - 프로그래머스
    """
    answer = 0

    answer += dfs(-numbers[0], 1, numbers, target)
    answer += dfs(numbers[0], 1, numbers, target)

    return answer


def dfs(prev, index, numbers, target):
    if index == len(numbers):
        if prev == target:
            return 1
        return 0

    count = 0
    count += dfs(-numbers[index] + prev, index + 1, numbers, target)
    count += dfs(numbers[index] + prev, index + 1, numbers, target)

    return count
