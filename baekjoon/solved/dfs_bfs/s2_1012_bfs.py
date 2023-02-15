from collections import deque

def bfs(graph : list, visited_list : list, start : tuple):
    x, y = start
    visited_list[x][y] = True
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            x_new = x + dx[i]
            y_new = y + dy[i]
            if 0 <= x_new < len(graph) and 0 <= y_new < len(graph[0])\
                and visited_list[x_new][y_new] == False:
                    if graph[x_new][y_new] == 1:
                        # 방문할 노드로 추가
                        queue.append([x_new, y_new])
                        # 방문 처리
                        visited_list[x_new][y_new] = True

test_case = int(input())
# 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(test_case):
    row_size, col_size, cab_num = map(int, input().split())
    
    graph = [[0] * col_size for _ in range(row_size)]
    visited_list = [[False] * col_size for _ in range(row_size)]
    
    for _ in range(cab_num):
        x, y = map(int, input().split())
        graph[x][y] = 1
        
    count = 0
    for col in range(col_size):
        for row in range(row_size):
            if graph[row][col] == 0:
                visited_list[row][col] = True
                continue
            else:
                if visited_list[row][col] == False:
                    bfs(graph, visited_list, (row, col))
                    count += 1
                    
    print(count)
    # 개수 초기화
    count = 0