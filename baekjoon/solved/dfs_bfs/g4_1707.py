from collections import deque
import sys
# 그래프 성분 정렬
import heapq

def bfs(graph : list, start : int):
    # 노드 종류 설정
    queue = deque()
    # bi : 한번은 0, 한번은 1로 구분
    # idx와 함께 넣어줌
    is_bi[start] = 0
    flag = 1
    queue.append([1, graph[start]])
    while queue:
        # idx와 연결된 점들
        flag, link = queue.popleft()
        #print(is_bi, start, link)
        for target in link:
            # 아직 방문하지 않은 경우   
            if is_bi[target] == -1:
                # 방문 처리
                is_bi[target] = flag
                # flag 설정
                new_flag = abs(1 - flag)
                queue.append([new_flag, graph[target]])
            # target의 flag가 설정한 flag와 다를 경우
            else:
                if is_bi[target] != flag:
                    return False
    return True
    
test_case = int(input())
for _ in range(test_case):
    node_num, edge_num = map(int, input().split())
    # 숫자를 그대로 인덱스로 활용
    graph = [[] for _ in range(node_num + 1)]
    #is_bi = [[False for _ in range(node_num + 1)] for _ in range(node_num + 1)]
    is_bi = [-1 for _ in range(node_num + 1)]
    for _ in range(edge_num):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        # 그래프 성분 정렬
        heapq.heappush(graph[start], end)
        heapq.heappush(graph[end], start)
    # 모든 정점 방문하도록
    for i in range(1, node_num):
        if is_bi[i] == -1:
            result = bfs(graph, i)
            if not result:
                print("NO")
                break
    else:
        print("YES")