def dfs(graph : list, visited_list : list, start : tuple):
    # 시작점 할당
    x, y = start
    # 방문 처리
    visited_list[x][y] = True
    # 개수 세기
    global count
    
    for i in range(4):
        # 새로운 좌표 이동
        x_new = x + dx[i]
        y_new = y + dy[i]
        # 정해진 graph를 벗어나지 않고 아직 방문하지 않은 경우
        if 0 <= x_new < len(graph) and 0 <= y_new < len(graph) and \
            visited_list[x_new][y_new] == False:
            # 집이 있는 경우
            if graph[x_new][y_new] == "1":
                # 개수 증가
                count += 1
                # 새로운 점에서 DFS 실행
                dfs(graph, visited_list, (x_new, y_new))
    return count

graph_size = int(input())
# 문자열을 한 글자씩 저장하기
# input()을 list로 감싸줌.
graph = [list(input()) for _ in range(graph_size)]
visited_list = [ ([False] * graph_size) for _ in range(graph_size)]
# 단지 내 집 개수 저장
count_list = []
count = 1
# 상하 이동
dx = [-1, 1, 0, 0]
# 좌우 이동
dy = [0, 0, -1, 1]

for col in range(graph_size):
    for row in range(graph_size):
        # 0이면 방문 처리만 하고 넘김
        if graph[row][col] == "0":
            visited_list[row][col] = True
        # 1이면 DFS로 조회
        else:
            # 아직 방문하지 않은 경우만 조회
            if not visited_list[row][col]:
                temp_count = dfs(graph, visited_list, (row, col))
                count_list.append(temp_count)
                count = 1

print(len(count_list), *sorted(count_list))
            
            