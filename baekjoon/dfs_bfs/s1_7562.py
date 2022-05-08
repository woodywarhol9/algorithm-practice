from collections import deque

def bfs(graph : list, queue : deque, target : list):
    while queue:
        x, y = queue.popleft()
        # 도달했을 경우 종료(시작, 끝이 있는 경우 지정)
        if x == target[0] and y == target[1]:
            break
        for i in range(8):
            x_new = x + dx[i]
            y_new = y + dy[i]
            if 0 <= x_new < graph_size and 0 <= y_new < graph_size and \
                graph[x_new][y_new] == 0:
                    graph[x_new][y_new] = graph[x][y] + 1
                    queue.append([x_new, y_new])
    
    
    print(graph[target[0]][target[1]])
# 나이트가 이동 가능한 점
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
test_case = int(input())
for _ in range(test_case):
    graph_size = int(input())
    graph = [[0] * graph_size for _ in range(graph_size)]
    # 시작점 설정
    start = tuple(map(int, input().split()))
    # 목표 지점 설정
    target = tuple(map(int, input().split()))
    
    queue = deque()
    queue.append(start)
    bfs(graph, queue, target)
    