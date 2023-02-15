from collections import deque

def bfs(x, y, graph, visited):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    # 넓이 계산
    area = 0
    while queue:
        x, y = queue.popleft()
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 방문 가능 조건
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1:
                # 아직 방문하지 않은 경우
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
    return area              

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 방문
max_area = 0
cnt = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1 and visited[x][y] == 0:
            temp_area = bfs(x, y, graph, visited)
            max_area = max(max_area, temp_area)
            cnt += 1

print(cnt, max_area, sep = "\n")