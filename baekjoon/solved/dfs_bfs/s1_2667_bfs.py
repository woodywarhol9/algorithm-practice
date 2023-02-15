from collections import deque

def bfs(graph : list, visited_list : list, start : list):
    # 카운트 개수 세기
    global count
    # 초기 좌표 설정 및 방문 처리
    x, y = start
    visited_list[x][y] = True
    # 큐에 초기 좌표 넣기
    queue = deque([start])
    while queue:
        # 좌표 설정 및 방문 처리
        x, y = queue.popleft()
        # 좌표 이동
        for i in range(4):
            x_new = x + dx[i]
            y_new = y + dy[i]
            # 새로운 좌표가 그래프 안의 점이면서 아직 방문하지 않았다면
            if 0 <= x_new < len(graph) and 0 <= y_new < len(graph) \
                and visited_list[x_new][y_new] == False:
                    # 만약 집이 있다면 bfs 실행
                    if graph[x_new][y_new] == "1":
                        queue.append((x_new, y_new))
                        visited_list[x_new][y_new] = True
                        count += 1
    return count

graph_size = int(input())
# 결고 받아와 쪼개기
graph = [list(input()) for _ in range(graph_size)]
visited_list = [[False] * graph_size for _ in range(graph_size)]
# 상, 하
dx = [-1, 1, 0, 0]
# 좌, 우 
dy = [0, 0, -1, 1]
# 결과 저장
count_list= []
# 개수 초기화
count = 1

for col in range(graph_size):
    for row in range(graph_size):
        # 0인 경우 True로 바꾸기만 하고 탐사 안함
        if graph[row][col] == "0":
            visited_list[row][col] = True
            continue
        else:
            # 아직 방문하지 않은 경우
            if not visited_list[row][col]:
                temp_count = bfs(graph, visited_list ,[row, col])
                count_list.append(temp_count)
                # 개수 초기화
                count = 1

print(len(count_list), *sorted(count_list))
