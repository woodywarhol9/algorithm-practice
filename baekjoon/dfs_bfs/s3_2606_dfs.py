def dfs(graph : list, visited_list : list, start : int):
    visited_list[start - 1] = True
    for node in graph[start - 1]:
        if not visited_list[node - 1]:
            dfs(graph, visited_list, node)

node_num = int(input())
edges_num = int(input())
edges_list = [list(map(int, input().split())) for i in range(edges_num)]

graph = []
visited_list = [False] * (node_num)

# 연결 리스트 구성
for node in range(1, node_num + 1):
    temp = []
    for edge in edges_list:
        if edge[0] == node:
            temp.append(edge[1])
        elif edge[1] == node:
            temp.append(edge[0])
    graph.append(sorted(temp))

dfs(graph, visited_list, 1)
print(sum([1 for i in visited_list if i == True]) - 1)