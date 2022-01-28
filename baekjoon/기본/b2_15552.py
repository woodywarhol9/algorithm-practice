import sys

# 빠른 입력
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)