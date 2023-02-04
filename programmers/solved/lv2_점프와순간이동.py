# 항상 순간 이동 하는 것이 이득
# 홀수라서 순간 이동 시 위치가 안 맞으면 그때 1씩 증가
def solution(n):
    answer = 0
    while n:
        q,r = divmod(n, 2)
        if r == 1:
            answer += 1
        n = q
    return answer
# DP를 활용한 풀이
"""
def solution(n):
    answer = [i for i in range(n + 1)]
    answer[0] = 1e9
    for i in range(2, n + 1):
        # 짝수일 경우
        if i % 2 == 0:
            answer[i] = min(answer[i], answer[i // 2])
        # 홀수일 경우
        else:
            answer[i] = min(answer[i], answer[i // 2] + 1)
    return answer[-1]
"""