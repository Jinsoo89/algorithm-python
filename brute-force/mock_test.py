def solution(answers):
    """
    프로그래머스 - 완전탐색 - '모의고사' 문제 풀이
    :param answers: 시험 문제의 정답이 순서대로 들어있는 배열
    :return: 가장 높은 점수를 받은 사람의 배열 (최고 득점자 복수 가능)
    """
    answer = []
    arr = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    count_arr = [0, 0, 0]

    for idx, ans in enumerate(answers):
        if ans == arr[0][idx % len(arr[0])]:
            count_arr[0] += 1
        if ans == arr[1][idx % len(arr[1])]:
            count_arr[1] += 1
        if ans == arr[2][idx % len(arr[2])]:
            count_arr[2] += 1

    for i in range(3):
        max_num = max(count_arr)

        if count_arr[i] == max_num:
            answer.append(i + 1)

    return answer
