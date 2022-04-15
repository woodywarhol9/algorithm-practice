import sys

n = int(input())
num_list = sys.stdin.readline().rstrip().split()
num_list = list(map(int, num_list))

rank = 0
mean_num = min(num_list)
num_rank = {}

for i in sorted(num_list):
    if i > mean_num:
        mean_num = i
        rank += 1
    num_rank[i] = rank

print(*[num_rank[i] for i in num_list])