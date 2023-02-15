import sys

virus_num, p, time = map(int, input().split())
# 나머지 성질 이용
for _ in range(time):
    virus_num *= p
    virus_num %= 1000000007
print(virus_num)