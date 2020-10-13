def solution(n, lost, reserve):
    for j in lost:
        if j in reserve:
            lost.remove(j)
            reserve.remove(j)

    answer = n - len(lost)

    for i in lost:
        if reserve.count(i) > 0:
            reserve.remove(i)
            answer += 1
        elif reserve.count(i - 1) > 0:
            reserve.remove(i - 1)
            answer += 1
        elif reserve.count(i + 1) > 0:
            reserve.remove(i + 1)
            answer += 1

    return answer
