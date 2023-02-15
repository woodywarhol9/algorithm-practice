from collections import deque

def bfs(graph : list, start : int, target : int):
    # 시작점 입력
    queue = deque()
    queue.append(start)
    # 횟수
    while queue:
        # 탐색 시작
        x = queue.popleft()
        if x == target:
            print(graph[target])
            break
        # for문을 돌릴 때 x * 2부터 돌리면 x = 0의 크기가 1로 변경돼 문제가 생김
        # 따라서 x - 1 또는 x + 1을 첫번째로.
        for x_new in (x - 1, x + 1, x * 2):
            if 0 <= x_new < len(graph) and graph[x_new] == 0:
                graph[x_new] = graph[x] + 1
                queue.append(x_new)
            
start, target = map(int, input().split())
graph = [0 for _ in range(100001)]
bfs(graph, start, target)