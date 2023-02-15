import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_sum = [0]
total = 0
for i in range(N):
    total += num_list[i]
    prefix_sum.append(total)
    
for _ in range(M):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[end] - prefix_sum[start - 1])