from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maps):
    
    queue = deque()
    queue.append([x, y])
    # queue 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 좌표 안에 있고, 벽 아니면
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[x][y] != 0:
                # 처음 방문하면
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1 
                    queue.append([nx, ny])


def solution(maps):
    bfs(0, 0, maps)
    x, y = len(maps) - 1, len(maps[0]) - 1
    answer = -1 if maps[x][y] == 1 else maps[x][y]
    return answer