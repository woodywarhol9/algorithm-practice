import sys
# recursion error 발생 시 활용
sys.setrecursionlimit(10**6)

def dfs(graph : list, visited_list : list, start : tuple):
    # 시작 점 
    x, y = start
    # 방문 처리
    visited_list[x][y] = True
    for i in range(4):
        x_new = x + dx[i]
        y_new = y + dy[i]
        # 좌표가 그래프 안에 있고 아직 방문하지 않은 점인 경우
        if 0 <= x_new < len(graph) and 0 <= y_new < len(graph[0]) \
            and visited_list[x_new][y_new] == False:
                # 배추가 있다면 탐색 시작
                if graph[x_new][y_new] == 1:
                    dfs(graph, visited_list, (x_new, y_new))

#test_case 수 만큼 반복
test_case = int(input())
# 상하
dx = [-1, 1, 0, 0]
# 좌우
dy = [0, 0, -1, 1]

for _ in range(test_case):
    row_size, col_size, cab_num = map(int, input().split())
    # 기본 그래프 그리기
    graph = [[0] * col_size for _ in range(row_size)]
    visited_list = [[False] * col_size for _ in range(row_size)]
    count = 0
    # 배추 위치 설정
    for _ in range(cab_num):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    for col in range(col_size):
        for row in range(row_size):
            if graph[row][col] == 0:
                visited_list[row][col] = True
                continue
            else:
                if visited_list[row][col] == False:
                    dfs(graph, visited_list, (row, col))
                    count += 1
    print(count)
    count = 0