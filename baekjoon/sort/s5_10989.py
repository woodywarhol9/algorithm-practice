"""
메모리 제한 주의!
"""


import sys

n = int(input())
n_list = [0] * 10000
# 많은 입력 처리
for i in range(n):
    n_list[int(sys.stdin.readline().rstrip()) - 1] += 1

for i in range(len(n_list)):
    for j in range(n_list[i]):
        print(i + 1)