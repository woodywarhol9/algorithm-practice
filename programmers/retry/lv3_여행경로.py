# 백트래킹 이용 풀이
from collections import defaultdict

def solution(tickets):
    # 방문 여부
    visited = defaultdict(list)
    # 그래프
    graph = defaultdict(list)
    start = "ICN"
    goal = len(tickets) + 1
    # 경로 정보
    answer = []
    # 그래프 정보 저장
    for ticket in tickets:
        a, b = ticket
        graph[a].append(b)
        visited[a].append(False)
    
    def dfs(now, path):
        nonlocal goal

        if len(path) == goal:
            answer.append(path)
            return  
        # 순차적으로 탐색
        for j in range(len(graph[now])):
            if not visited[now][j]:
                # 아직 방문하지 않은 경우
                nxt = graph[now][j]
                visited[now][j] = True
                dfs(nxt, path + [nxt])
                visited[now][j] = False
    # 시작은 무조건 ICN
    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]

# 도시 정렬 활용
from collections import deque, defaultdict

def dfs(graph):
    # 시작점 입력
    stack = deque()
    stack.append("ICN")   
    path = []
    while stack:
        # 출발 도시
        start = stack.pop()
        # 더이상 출발 - 도착 불가능할 경우 path에 저장
        if start not in graph or not graph[start]:
            path.append(start)
        # 방문 가능할 경우
        else:
            stack.append(start)
            stack.append(graph[start].pop())
    return path[::-1]
            
def solution(tickets):
    # 그래프 생성
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    # 도착 리스크 역순 정렬
    # DFS에서 먼저 선택될 수 있도록
    for k in graph.keys():
        graph[k].sort(reverse = True)
    answer = dfs(graph)
    return answer