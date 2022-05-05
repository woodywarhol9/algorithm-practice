"""
이동 거리를 graph에 저장하면서 진행하면 마지막 점에 이동 거리를 얻을 수 있음.
최소 거리를 계산해야 하기 때문에 방문 처리 진행.
"""
from collections import deque

def bfs(graph : list, visited_list : list, start : tuple):
    # 첫 좌표 방문 처리
    x, y = start
    visited_list[x][y] = True
    queue = deque([start]) 
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            x_new = x + dx[i]
            y_new = y + dy[i]
            if 0 <= x_new < row_size and 0 <= y_new < col_size \
                and visited_list[x_new][y_new] == False:
                    # 최단 거리 저장
                    if graph[x_new][y_new] == 1:
                        visited_list[x_new][y_new] = True
                        graph[x_new][y_new] = graph[x][y] + 1
                        queue.append([x_new, y_new])
    
    print(graph[row_size - 1][col_size - 1])
    

row_size, col_size = map(int, input().split())
graph = [list(map(int, input())) for _ in range(row_size)]
visited_list = [[False] * col_size for _ in range(row_size)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(graph, visited_list,(0,0))