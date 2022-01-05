"""
특정 거리의 도시 찾기 : 플로이드 워셜로 풀이
"""
INF = int(1e9)
# N, M, K, X : 도시의 개수, 도로의 개수, 거리 정보, 출발 도시
N, M, K, X = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(M):
    # A에서 B로 가는 비용은 C라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for c in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])
            
# 경로 존재하는지 확인
count = 0
for b in range(1, N + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if graph[X][b] == K:
        print(b)
        count += 1
        # 도달할 수 있는 경우 거리를 출력

if count == 0:
    print("-1")

