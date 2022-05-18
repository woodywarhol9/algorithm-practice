import sys
from collections import deque

def bfs(queue):
    num = 0
    while queue:
        x, y = queue.popleft()
        num += 1
        for i in range(4):
            x_new = x + dx[i]
            y_new = y + dy[i]
            # 방문 아직 하지 않은 점이 그래프 안에 있을 경우
            if 0<= x_new < graph_size and 0<= y_new < graph_size and graph[x_new][y_new] == "1":
                queue.append([x_new, y_new])
                # 이때 방문 처리해야 함. queue이기 때문에 나중에 처리될 수도 있음.
                graph[x_new][y_new] = "0"
    return num


# 상하 좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 그래프 생성
graph_size = int(input())
graph = [list(input()) for _ in range(graph_size)]
# 탐색 수
count = 0

queue = deque()
num_list = []
for row in range(graph_size):
    for col in range(graph_size):
        if graph[row][col] == "1":
            graph[row][col] = 0
            queue.append([row, col])
            num = bfs(queue)
            # 탐색 개수
            num_list.append(num)
            # 블록 수
            count += 1

print(count)
print(*sorted(num_list), sep = "\n")
