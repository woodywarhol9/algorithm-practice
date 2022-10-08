from collections import deque

def bfs(graph, visited, n, start):
    # BFS 탐색
    queue = deque()
    queue.append(start)
    # 방문 처리
    visited[start] = True
    while queue:
        # 방문 처리
        node = queue.popleft()
        # 방문할 지점
        for end in range(n):
            if node != end and graph[node][end] == 1:
                if visited[end] == False:
                    queue.append(end)
                    visited[end] = True
    
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        # 아직 방문하지 않은 경우
        if visited[i] == False:
            bfs(computers, visited, n, i)
            answer += 1
    return answer