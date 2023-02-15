"""
입력 개수가 많으면 sys.stdin.readline().rstrip()으로 받기.
"""

import sys

n = int(input())
n_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
n_list.sort()
print(*n_list, sep = "\n")