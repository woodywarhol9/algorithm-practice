"""
도시 분할 계획 : 크루스칼 알고리즘. 어떻게 해야 최소 신장 트리를 2개의 부분 그래프로 나눌 수 있을 지 생각!
"""

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 엣지의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 모든 엣지를 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 초기화
for i in range(1, n + 1):
    parent[i] = i

# 모든 엣지에 대한 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 엣지를 비용순으로 정렬
edges.sort(key = lambda x : x[0])
last = 0 # 최소 신장 트리에 포함되는 엣지 중에서 가장 비용이 큰 엣지

# 엣지를 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
        
print(result - last)