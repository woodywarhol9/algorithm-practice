from collections import deque
def bfs(graph : list, queue : deque):
    while queue:
        # 좌표 초기화
        z, x, y= queue.popleft()
        for i in range(6):
            x_new = x + dx[i]
            y_new = y + dy[i]
            z_new = z + dz[i]
            if 0 <= x_new < row_size and 0 <= y_new < col_size \
                and 0 <= z_new < height_size and graph[z_new][x_new][y_new] == 0:
                    graph[z_new][x_new][y_new] = graph[z][x][y] + 1
                    queue.append([z_new, x_new, y_new])
    return

# x, y, z 축 까지 이동
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

col_size, row_size, height_size = map(int, input().split())
# 3중 리스트 생성 z -> x -> y 순
graph = [[list(map(int, input().split())) for _ in range(row_size)] \
    for _ in range(height_size)]
queue = deque()
# 3중 리스트 조회 z -> x -> y 순
for height in range(height_size):
    for row in range(row_size):
        for col in range(col_size):
            if graph[height][row][col] == 1:
                queue.append([height, row, col])

bfs(graph, queue)
# 최댓값 조회
max_result = 0
max_col = 0

for height in graph:
    for row in height:
        for col in row:
            if col == 0:
                print(-1)
                exit(0)
        # 행에서의 최댓값        
        max_col = max(max_col, max(row))
    # z에서의 최댓값
    max_result = max(max_result, max_col)

# for문이 올바르게 끝났을 경우
else:
    print(max_result - 1)
    