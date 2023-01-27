def solution(sizes):
    answer = map(sorted, sizes)
    answer = list(map(max, zip(*answer)))
    return answer[0] * answer[1]