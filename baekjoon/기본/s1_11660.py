import sys

n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
# 구간 합 계산
for row in range(1, n + 1):
    for col in range(1, n + 1):
        prefix_sum[row][col] = prefix_sum[row - 1][col] + prefix_sum[row][col - 1] - prefix_sum[row -1][col - 1] + graph[row - 1][col - 1]
# x1 ~ y1 구간이 두번 빼지기 때문에 더해줘야 함
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1])