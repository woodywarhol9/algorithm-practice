"""
포맷팅에서 정렬을 할 때에는 변수가 아닌 정수만 가능.
"""
N = int(input())

for i in range(N):
    print(" " * (N - i - 1) + "*" * (i + 1))