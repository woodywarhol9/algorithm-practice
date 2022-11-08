import sys

N = int(input())
A_list = list(map(int, sys.stdin.readline().split()))
B, C = map(int, input().split())

# 총 감독 배치
answer = 0
A_list = [(i - B) for i in A_list if (i - B) > 0]
answer += N

# 보조 감독 배치
for i in A_list:
    q, r = divmod(i, C)
    answer += q
    if r != 0:
        answer += 1

print(answer)