"""
경쟁적 전염 :
"""

"""
아이디어 : BFS 방식으로 최소 경로 확인한다. 
- 기존 코드에 visit 여부 확인하는 코드를 넣어서 불필요하게 반복되는 계산을 줄였다. 
"""
from collections import deque 

# 맵 크기, 바이러스 종류의 수 입력
N, K = map(int, input().split())

graph = [] # 시험관 정보
data = [] # 바이러스 정보

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))
            
# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 퍼지기 때문에)
data.sort(key = lambda x : x[0])
q = deque(data)

target_s, target_x, target_y = map(int, input().split())
            
#4 가지 이동 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]

# BFS 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            # 아직 방문하지 않은 위치면 바이러스 전염
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])