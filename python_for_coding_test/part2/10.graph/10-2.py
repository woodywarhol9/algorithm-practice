"""
경로 압축 기법 : 루트 노드를 바로 바꿔줘 불필요한 반복을 줄여준다.
"""
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]