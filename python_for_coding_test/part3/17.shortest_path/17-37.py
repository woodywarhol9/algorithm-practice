"""
플로이드 : 플로이드 워셜. 엣지가 1개 이상일 경우 최단 엣지만 고려.
"""
INF = int(1e9) # 무한 값

# 노드의 개수 및 엣지의 개수 입력
n = int(input())
m = int(input())
# 비용 테이블 초기화
cost = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            cost[a][b] = 0

# 각 엣지에 대한 정보 입력받아 초기화
for _ in range(m):
    # 출발 도시, 도착 도시, 비용 순으로 저장
    a, b, c = map(int, input().split())
    # 가장 짧은 간선 정보만 저장
    if c < cost[a][b]:
        cost[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            cost[a][b] = min(cost[a][b], cost[a][k] + cost[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
        if cost[a][b] == INF:
            print(0, end = " ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(cost[a][b], end = " ")
    print()