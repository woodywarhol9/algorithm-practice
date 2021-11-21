"""
    아이디어 : BFS로 탐색 구현 
    -> 탐색 순서 = 추출 순서
"""

from collections import deque

#BFS method
def bfs(graph, start, visited):
    queue = deque([start]) #노드 시작
    visited[start] = True #방문 처리
    
    #queue가 빌 때까지 반복
    while queue: 
        #queue에서 추출된 원소 출력()
        v= queue.popleft()
        print(v, end=' ')
        #해당 원소와 연결된 원소들을 queue에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# node : 1st~8th                
graph = [
    [], #0
    [2, 3, 8], #1
    [1, 7], #2
    [1, 4, 5], #3
    [3, 5], #4
    [3, 4], #5
    [7], #6
    [2, 6, 8], #7
    [1, 7] #8
]

#방문 여부 저장
visited = [False] * 9

bfs(graph, 1, visited)