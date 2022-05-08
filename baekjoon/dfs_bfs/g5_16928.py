from collections import deque

def bfs(graph : list):
    
    queue = deque()
    queue.append(1)
    
    while queue:
        x = queue.popleft()
        if x == 100:
            print(graph[100])
            return
        for x_new in (x + 1, x + 2, x + 3, x + 4, x + 5, x + 6):
            if 0 <= x_new < 101 and graph[x_new] == 0:
                graph[x_new] = graph[x] + 1
                # 사다리가 있을 경우
                if x_new in ladder_dict:
                    x_ladder = ladder_dict[x_new]
                    # 이동한 점이 아직 방문 안한 경우
                    if graph[x_ladder] == 0:
                        graph[x_ladder] = graph[x_new]
                        queue.append(x_ladder)
                # 뱀이 있을 경우
                elif x_new in snake_dict:
                    x_snake = snake_dict[x_new]
                    # 이동한 점이 아직 방문 안한 경우
                    if graph[x_snake] == 0:
                        graph[x_snake] = graph[x_new]
                        queue.append(x_snake)
                # 아무 것도 없을 경우
                else:
                    queue.append(x_new)
        
graph = [0] * 101
ladder, snake = map(int, input().split())
# 사다리 정보 입력
ladder_dict = {}
for _ in range(ladder):
    low, high = map(int, input().split())
    ladder_dict[low] = high
# 뱀 정보 입력
snake_dict = {}
for _ in range(snake):
    high, low = map(int, input().split())
    snake_dict[high] = low

bfs(graph)