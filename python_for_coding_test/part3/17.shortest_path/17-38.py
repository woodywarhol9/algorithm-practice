"""
정확한 순위 : 비교가 가능 == A -> B, B -> A 둘 경우 모두 도달 가능.
"""
INF = int(1e9) 

# 노드의 개수 및 엣지의 개수를 입력 받기
n, m = map(int, input().split())
#  2차원 그래프 생성, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 엣지에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # 대소 관계 입력
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
            
result = 0
# 도달 가능한 지 체크
for a in range(1, n + 1):
    count = 0
    for b in range(1, n + 1):
        # A - B가 연결 돼있으면 카운트 +1
        # 연결돼 있다면 도달 거리는 다르더라도 INF는 아니다!
        if graph[a][b] != INF or graph[b][a] != INF:
            count += 1
        # 도달할 수 있는 경우 거리를 출력
    if count == n:
        result += 1
print(result)