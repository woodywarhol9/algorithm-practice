"""
팀 결성 : 서로소 알고리즘 활용하기.
"""
n, m = map(int, input().split())

# 경로 압축 기법을 적용해 특정 원소가 속한 집합을 찾기
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

parent = [0] * (n + 1) # 부모 테이블 생성

# 부모 테이블 초기화
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    # f : find일때 1로 설정
    f, a, b = map(int, input().split())
    if f == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
