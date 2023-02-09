# n이 크기 때문에, n**2만 해도 시간 초과 발생!
# 규칙을 찾아야 함
# 1     2       3       2       2       3       3       3       3
# (0,0) (0,1)   (0,2)   (1, 0)  (1, 1)  (1, 2)  (2, 0)  (2, 1)  (2, 2)
# 행렬 : 몫, 나머지로 표현된다고 생각 가능!
def solution(n, left, right):
    answer = [max(i // n, i % n) + 1 for i in range(left, right + 1)]
    return answer