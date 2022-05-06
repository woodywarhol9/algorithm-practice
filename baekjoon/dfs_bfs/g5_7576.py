from collections import deque 
import sys

def bfs(graph : list, start_point : deque):
    queue = start_point
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 이동할 좌표
            x_new = x + dx[i]
            y_new = y + dy[i]
            if 0 <= x_new < row_size and 0 <= y_new < col_size\
                and graph[x_new][y_new] == 0:
                    graph[x_new][y_new] = graph[x][y] + 1
                    queue.append([x_new, y_new])
        
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

col_size, row_size = map(int, input().split())
# graph 입력 받기
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(row_size)]
# 1이 담긴 점 queue에 담기 : 1이 담긴 모든 점에서 탐색 
start_point = deque()
# 행 -> 열 순으로 탐색
for row in range(row_size):
    for col in range(col_size):
        if graph[row][col] == 1:
            start_point.append([row, col])

bfs(graph, start_point)

max_result = 0
# 행 -> 열 순으로 탐색
for row in graph:
    for num in row:
        if num == 0:
            print(-1)
            exit(0)
    max_result = max(max_result, max(row))
    
else:
    print(max_result - 1)