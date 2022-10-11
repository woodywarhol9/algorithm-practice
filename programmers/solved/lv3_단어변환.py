from collections import deque

def bfs(start, end, graph, visited):
    # 시작점 입력 + 방문 처리
    queue = deque()
    queue.append([start, 1])
    visited[start] = 1
    
    while queue:
        node, cnt = queue.popleft()
        if node == end:
            return cnt
        else:
            for next in graph[node]:
                if not visited[next]:
                    queue.append([next, cnt + 1])
                    visited[next] = 1
    return 0
            
def solution(begin, target, words):
    # answer = 0
    graph = {}
    word_len = len(target)
    visited = dict(zip(words, [0] * len(words)))
    # 그래프 구성
    for i, key in enumerate(words):
        graph[key] = []
        for j, val in enumerate(words):
            cnt = 0
            if i == j: continue
            for k in range(word_len):
                # 거리 확인
                if key[k] != val[k]:
                    cnt += 1
                # 거리 1 넘으면 제거
                if cnt > 1:
                    break
            else:
                graph[key].append(val)
    # 방문 시작
    for node, _ in graph.items():
        cnt = 0
        for i in range(word_len):
            if begin[i] != node[i]:
                cnt += 1
            if cnt > 1:
                break
        else:
            answer = bfs(node, target, graph, visited)

    return answer