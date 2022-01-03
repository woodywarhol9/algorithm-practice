"""
아이디어 : BFS 방식으로 최소 경로 확인한다. 
- 기존 코드에 visit 여부 확인하는 코드를 넣어서 불필요하게 반복되는 계산을 줄였다. 
"""
from collections import deque 
import numpy as np

#map 정보 입력
n, m = 5, 6
#방문 여부
visit = np.zeros((n,m))
visit[0,0] = 1

graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

#이동 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]

#BFS 
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    #queue가 빌 때까지 반복
    while queue:
        print(queue)
        x, y = queue.popleft()
        #네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >=n or ny>= m:
                continue
            #벽 무시
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and visit[nx][ny] == 0:               
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                visit[nx][ny] += 1
    
    print(visit)
    return graph[n-1][m-1]

print(bfs(0,0))