"""
숨바꼭질 : 
"""

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 통로 개수 입력 받기
n, m = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보 담기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)
# 시작 노드 설정
start = 1

# 모든 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    # 양방향이므로
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않은 경우
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
# 다익스트라 알고리즘을 수행
dijkstra(start)


# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 거리
max_distance = 0

print(distance[1:])

for d in distance[1:]:
    if d >= max_distance:
        max_distance = max(max_distance, d)

# 헛간 번호
barn_idx = distance.index(max_distance)
barn_count = distance.count(max_distance)
        
# 시작 노드는 제외해야 하므로 count -1 을 출력
print(barn_idx, max_distance, barn_count)