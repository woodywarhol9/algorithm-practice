"""
node는 숫자이고 graph, visited는 행렬, list이다.
따라서 graph와 visited를 처리할 때만 node - 1 해주면 된다.
"""
from collections import deque

def dfs(graph : list, start : int, visited : list):
    # 방문 처리가 계속 전달돼야 함.
    visited[start - 1] = True
    print(start, end = " ")
    for node in graph[start - 1]:
        if not visited[node - 1]:
            # 방문하지 않은 점이 새로운 dfs의 시작점이 됨.
            dfs(graph, node, visited)
            
def bfs(graph : list, start : int):
    # 방문 처리 초기화
    visited = [False] * len(graph)
    visited[start - 1] = True
    # 초기 위치 queue에 삽입
    queue = deque([start - 1])
    while queue:
        pop = queue.popleft()
        print(pop, end = " ")
        for node in graph[pop]:
            if not visited[node - 1]:
                queue.append(node - 1)
                visited[node - 1] = True
                print(node, end = " ")
    
    
        
node, edge, start = map(int, input().split())
# 엣지 정보
edge_list = [list(map(int, input().split())) for _ in range(edge)]
# 그래프
graph = []
visited = [False] * node
# 그래프 정보 입력
for n in range(node):
    temp = []
    for e in edge_list:
        if n + 1 == e[0]:
            temp.append(e[1])
        elif n + 1 == e[1]:
            temp.append(e[0])
    # adj list 형태로 graph 저장
    graph.append(sorted(temp))

dfs(graph, start, visited)
print("")
bfs(graph, start)
    