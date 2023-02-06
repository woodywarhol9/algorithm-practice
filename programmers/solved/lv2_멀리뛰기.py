# 가능한 모든 방법의 수
# a1 = 1
# an = a(n - 1) + a(n - 2)
def solution(n):
    answer = [i for i in range(n + 1)]
    for i in range(3, n + 1):
        answer[i] = answer[i - 1] + answer[i - 2]
    return answer[n] % 1234567