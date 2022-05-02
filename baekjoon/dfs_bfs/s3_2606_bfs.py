from collections import deque

def bfs(graph : list, visited_list : list, start : int):
    visited_list[start - 1] = False
    queue = deque([start - 1])
    while queue:
        pop = queue.popleft()
        for node in graph[pop]:
            if not visited_list[node - 1]:
                queue.append(node - 1)
                visited_list[node - 1] = True

nodes_num = int(input())
edges_num = int(input())
edges_list = [list(map(int, input().split())) for _ in range(edges_num)]

graph = []
visited_list = [False] * (nodes_num)
for node in range(1, nodes_num + 1):
    temp = []
    for edge in edges_list:
        if edge[0] == node:
            temp.append(edge[1])
        elif edge[1] == node:
            temp.append(edge[0])
    # 연결 리스트 추가
    graph.append(sorted(temp))

bfs(graph, visited_list, 1)
print(sum([1 for i in visited_list if i == True]) - 1)
    