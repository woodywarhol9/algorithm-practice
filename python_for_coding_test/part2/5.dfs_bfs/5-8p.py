"""
아이디어 : 재귀를 이용해 DFS로 탐색을 구현한다.
"""

#DFS method
def dfs(graph, v, visited):
    #현재 노드 방문 처리
    visited[v] = True
    print(v, end = " ")
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited) #i 노드에 대해서 dfs 진행
            
# node : 1st~8th                
graph = [
    [], #0
    [2, 3, 8], #1
    [1, 7], #2
    [1, 4, 5], #3
    [3, 5], #4
    [3, 4], #5
    [7], #6
    [2, 6, 8], #7
    [1, 7] #8
]

#방문 여부 저장
visited = [False] * 9

dfs(graph, 1, visited)
    
    