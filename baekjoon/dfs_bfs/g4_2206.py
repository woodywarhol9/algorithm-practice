from collections import deque
#import copy

def bfs(graph):
    queue = deque()
    # 시작점, 벽 부수기 여부
    queue.append([0, 0, 0])
    while queue:
        # 시작점, 벽 부수기 여부
        x, y, wall = queue.popleft()
        #print(graph)
        if x == row_size - 1 and y == col_size - 1:
            print(graph[wall][row_size - 1][col_size - 1] + 1)
            return
        for i in range(4):
            x_new = x + dx[i]
            y_new = y + dy[i]
            if 0 <= x_new < row_size and 0 <= y_new < col_size:
                if graph[wall][x_new][y_new] == 1:
                    # 벽이 막혀 있는 경우
                    if wall == 0:
                        graph[1][x_new][y_new] = graph[wall][x][y] + 1
                        queue.append([x_new, y_new, 1])
                    
                elif graph[wall][x_new][y_new] == 0:
                    graph[wall][x_new][y_new] = graph[wall][x][y] + 1
                    # 기존 벽 정보 그대로 넣기(안 부셨거나 부셨거나)
                    queue.append([x_new, y_new, wall])
    else:
        print(-1)
# 상하, 좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

row_size, col_size = map(int, input().split())
graph = [list(map(int, input())) for _ in range(row_size)]
# graph = [copy.deepcopy(graph) for _ in range(2)] 
graph_flag = []
for _ in range(2):
    graph_flag.append([val[:] for val in graph])

bfs(graph_flag)